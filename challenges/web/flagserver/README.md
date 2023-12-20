# FlagServer

- 作者：13m0n4de
- 参考：-
- 难度：Baby/Trivial/Easy/Normal/Medium/Hard/Expert/Insane
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
