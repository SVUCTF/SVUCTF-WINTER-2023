# 猫娘问答

- 作者：13m0n4de
- 参考：[USTC-Hackergame-2023-猫咪小测](https://github.com/USTC-Hackergame/hackergame2023-writeups/blob/master/official/%E7%8C%AB%E5%92%AA%E5%B0%8F%E6%B5%8B/README.md)
- 难度：Normal
- 分类：Misc
- 镜像：[svuctf-winter-2023/neko_quiz](https://ghcr.io/svuctf/svuctf-winter-2023/neko_quiz)
- 端口：3000

## 题目描述

圣诞快乐喵~

## 题目解析

题目形式仿照 [USTC-Hackergame-2023-猫咪小测](https://github.com/USTC-Hackergame/hackergame2023-writeups/blob/master/official/%E7%8C%AB%E5%92%AA%E5%B0%8F%E6%B5%8B/README.md)，可以去翻看一下历届的猫咪小测/猫咪问答，对这类搜索题目有进一步的了解。

题目框架开源在 [13m0n4de/neko-quiz](https://github.com/13m0n4de/neko-quiz) ，欢迎提意见。

下面是题目解析：

______________________________________________________________________

> 1\. 2023 年 11 月，第十四届江苏省大学生机器人大赛在我校成功举办，此次比赛共有多少支代表队参加？**（30 分）**
>
> 提示：非负整数，例：100

答案：`469`

在搜索引擎中搜索关键词 `第十四届江苏省大学生机器人大赛`，检索结果大多来自各个参赛学校官网，其中就有作为承办方的我校。

如果搜索结果太杂乱，可以加上 `site:jssvc.edu.cn` 限定结果来自我校官网，第一条结果是：[第十四届江苏省大学生机器人大赛在我校成功举办](https://www.jssvc.edu.cn/xww/xxyw/202311/t20231108_263299.shtml) 。

代表队数量在文章开头：

![校内文章](writeup/%E6%A0%A1%E5%86%85%E6%96%87%E7%AB%A0.png)

一些外文引擎暂时还没有收录这些中文内容，不太好搜，建议使用必应。

但并不是离开搜索引擎就彻底没办法了，重大比赛的承办，学校官网一定会发文的，可以使用学校官网自带的站内搜索，也能直接得到结果：

![站内搜索](writeup/%E7%AB%99%E5%86%85%E6%90%9C%E7%B4%A2.png)

______________________________________________________________________

> 2\. 截至 2023-12-01 日，SVUCTF 新生赛 GitHub 仓库中的最后一次提交（commit）的哈希值为？**（30 分）**
>
> 提示：例：c06083e6f712b2ee24b7639a2ba7b2b158b7e157

答案：`c9376fd461e00f3e1899a4435839691b7aed3de8`

Git 和 GitHub 的使用是必要的前置知识，如果你对它们还一无所知，可以看[这篇文章](https://www.freecodecamp.org/chinese/news/git-and-github-for-beginners/)来简单了解。

在 Git 仓库进行提交（commit）时，Git 会生成唯一的 *commit hash* ，用于标识此次提交。

它是由 SHA-1 哈希算法计算得出的一串 40 位 16 进制数字，比如示例中的 `c06083e6f712b2ee24b7639a2ba7b2b158b7e157`，就是 `svuctf` 进行 SHA-1 计算之后的结果。

在 SVUCTF 新生赛仓库 [SVUCTF/SVUCTF-HELLOWORLD-2023](https://github.com/SVUCTF/SVUCTF-HELLOWORLD-2023) 页面，点击提交历史按钮：

![提交按钮](writeup/%E6%8F%90%E4%BA%A4%E6%8C%89%E9%92%AE.png)

可以看到提交的时间线：

![提交时间线](writeup/%E6%8F%90%E4%BA%A4%E6%97%B6%E9%97%B4%E7%BA%BF.png)

而 2023-12-01 日之前的最后一次提交是 SVUCTF 用户的 [Update LICENSE](https://github.com/SVUCTF/SVUCTF-HELLOWORLD-2023/commit/c9376fd461e00f3e1899a4435839691b7aed3de8)，右侧 `c9376fd` 是 *commit hash* 的前七位，点击旁边的复制按钮就可以复制完整的 *commit hash* 了。

如果不在页面上操作也是可以的，首先**克隆**仓库到本地，使用 `git log` 命令可以看到历史 commit 的哈希值：

```
commit c9376fd461e00f3e1899a4435839691b7aed3de8
Author: SVUCTF <145646018+SVUCTF@users.noreply.github.com>
Date:   Sun Nov 5 18:56:11 2023 +0800

    Update LICENSE

    更换 GPL 许可证
```

*题外话：*

此次提交是变更了仓库的许可证，从 MIT 更换为了 GPLv3 ，因为[有一题](https://github.com/SVUCTF/SVUCTF-HELLOWORLD-2023/tree/main/challenges/web/missile_trail)借用了其他比赛的源文件，而那个源文件以 GPL 许可证开源。

GPL 许可证的其中一个特性是：如果某个项目使用了以 GPL 许可证开源的代码，那么它的源代码也必须开源，且也要使用 GPL 许可证。

所以那题的部分需要用 GPLv3 许可证，于是干脆整个仓库都更新为 GPLv3 许可证了。

不同的开源许可证有不同的约束，希望同学们都能遵守开源协议。

______________________________________________________________________

> 3\. IDA Pro 的图标是哪位女子？**（20 分）**
>
> 提示：填写完整的本名（简体中文译名），例：爱丽丝·玛格特罗依德

答案：`弗朗索瓦兹·多比涅` 或 `弗朗索瓦兹·奥比涅` 或 `弗朗索瓦丝·多比涅`

将题目原封不动放入搜索引擎，可以找到一个知乎提问：[IDA图标的头像是谁？ - 知乎](https://www.zhihu.com/question/41774725)。

首个回答中先是说 IDA 图标是 Ada Lovelace ，世界第一位女程序员，但评论区有人指正：

> 然而并不是..Ada Lovelace的头像是有皇家版权的. 所以IDA用了另一个女性的头像: Marquise de Maintenon

到底哪个是真的？

如果使用 `IDA 图标 是谁` 再仔细搜索过，可以找到这样一篇文章：[IDA pro的icon不是第一位程序媛Ada Lovelace](https://blog.airmole.cn/2018/02/20/IDA-pro%E7%9A%84icon%E4%B8%8D%E6%98%AF%E7%AC%AC%E4%B8%80%E4%BD%8D%E7%A8%8B%E5%BA%8F%E5%AA%9BAda-Lovelace/)

文章作者在 StackExchange上找到了答案：

> FWIW, the IDA logo came from a mid-90s image CD called “10000  royalty free images”, probably some so-so scan of the old picture now  shown on the wikipedia (this is the first time I see it on the web btw). I would have wanted a royalty free picture of Ada Lovelace for whom I  couldn’t find a royalty free image at the time…

> 当时（1999年）在网上找不到Ada的免费照片，于是就用了一张法皇路易14的第二个妻子Marquise de Maintenon的免费照片作为IDA Pro的logo，并沿用至今。

虽然作者截图中的提问已经找不到了，但其中回答的人 [Igor Skochinsky](https://stackexchange.com/users/185833/igor-skochinsky) 还能找到，他在 Hex-Rays 工作，可信度还是挺高的。

所以这个女人是法皇路易十四的第二个妻子 Marquise de Maintenon **曼特农夫人**。

但是 曼特农夫人 不是题目想要的答案，要求她的本名，且要中文译名。

从维基或者百度百科等途径都可以找到简体中文的本名：`弗朗索瓦兹·多比涅` 或 `弗朗索瓦兹·奥比涅` 或 `弗朗索瓦丝·多比涅`。

题目只认定这三种是正确答案，它们应该是网上最常见的几个译名。

当然，从一开始就使用以图搜图的功能搜索 IDA Pro 的图标，也是个好办法。

[Madame de Maintenon looking back by Marie Victoire Jaquotot after Pierre Mignard (Musée du Louvre - Paris France)](https://www.gogmsite.net/end_of_the_era_-_1684_to_17/subalbum_francoise_daubigne/madame-de-maintenon-looking.html)

______________________________________________________________________

> 4\. 为了将全世界无数物理层网络上的比特流拟人化，RFC 提出了一个 TCP 选项来表达数据包情绪，当向连接的系统发送 RST 数据包时，应该在此选项处填入什么内容？**（20 分）**
>
> 提示：表情符号，例：;)

答案：`:|`

首先什么是 RFC ：

> Request For  Comments（RFC），是一系列以编号排定的文件。文件收集了有关互联网相关信息，以及UNIX和互联网社区的软件文件。RFC文件是由Internet  Society（ISOC）赞助发行。基本的互联网通信协议都有在RFC文件内详细说明。RFC文件还额外加入许多在标准内的论题，例如对于互联网新开发的协议及发展中所有的记录。因此几乎所有的互联网标准都有收录在RFC文件之中。

RFC 文档包含了计算机网络的方方面面，绝大部分网络标准的制定都是以 RFC 的形式开始。

但 RFC 也并非全部是严肃的技术文件，偶尔也有恶搞之作，通常发布在 4 月 1 日愚人节，每一篇都乍有其事地拟定各项标准。

例如：

- RFC 1149： 鸽载互联网协议。以鸽子作为载体传输数据，传输可靠性差，鸟类容易受到天气和环境等因素的影响，如遇极端天气，丢包率可高达100%...

- RFC 1606：从历史的角度看 IPv9 的使用。文档中称过去几年里 IPv9 的普及率惊人，但由于太阳系上智能生命以及超光速传输堆栈的并行发现使可用空间急剧减少，把 IPv9 可寻址组件注射到血流中还不确定...

- RFC 2324：超文本咖啡壶控制协议（HTCPCP）。制定了一系列控制联网咖啡壶的协议，甚至真的衍生出了 418 这个 HTTP 状态码...

本题的 TCP 包的情绪选项很显然也是一部恶搞作品，那我们的首要目标就是找到对应的 RFC 文档。

搜索 `RFC TCP option emotion` 或者 `RFC TCP option denote` 可以找到 [RFC 5841: TCP Option to Denote Packet Mood](https://www.rfc-editor.org/rfc/rfc5841) 。

全文搜索 `RST` 找到 4.10 章节：

> ##### 4.10. Apathetic Packets
>
> When sending a RST packet to a connected system, the packet should be  marked as apathetic so that the receiver knows that your system does not care what happens after that.

当向连接的系统发送 RST 数据包时，应该将此数据包标记为“冷漠”（`apathetic`）。

在第 3 节简单情绪表征中，列出了传达情绪时建议使用的 ASCII 表情：

> ```
> ASCII                Mood
> =====                ====
> :)                   Happy
> :(                   Sad
> :D                   Amused
> %(                   Confused
> :o                   Bored
> :O                   Surprised
> :P                   Silly
> :@                   Frustrated
> >:@                  Angry
> :|                   Apathetic
> ;)                   Sneaky
> >:)                  Evil
> ```

`Apathetic` 应该使用 `:|`

## 非预期

本以为是抢跑，结果是非预期。

框架后端判断逻辑写的有问题，见：https://github.com/13m0n4de/neko-quiz/blob/46ff2ee5319ea91cf1a6560af83698602d32635d/backend/src/main.rs#L102-L115

```rust
    let correct_answers = ANSWERS.get().unwrap();

    let mut status = true;
    let mut score = 0;

    for user_answer in user_answers {
        if let Some((correct_answer, points)) = correct_answers.get(&user_answer.id) {
            if correct_answer.contains(&user_answer.answer) {
                score += points;
            } else {
                status = false;
            }
        }
    }
```

`status` 变量代表是否获得 Flag，默认是 `true` 。

如果 `user_answers` 列表为空，不进入循环，或者只传入一两个正确的题目，`status` 是不会变为 `false` 的。

意味着提交：

```
[]
或
[{"id":1,"answer":"469"}]
```

都是可以直接得到 Flag 的。

选手 write-up 中说的“抓包了一下，再点击提交，做着做着就出来了”，应该就是这样吧。

现在已经修复，https://github.com/13m0n4de/neko-quiz/commit/0dba01323911d87cb6a8b5d2f66a373a7fbe98f5 ，改成了：

```rust
    let user_answers: HashMap<usize, String> = HashMap::from_iter(
        request_answers
            .iter()
            .cloned()
            .map(|AnswerRequest { id, answer }| (id, answer)),
    );

    let mut status = true;
    let mut score = 0;

    for (id, (correct_answer, points)) in correct_answers {
        match user_answers.get(id) {
            Some(answer) if correct_answer.contains(answer) => score += points,
            _ => status = false,
        }
    }
```

仓库附件、镜像，包括平台的镜像也更新了，想要复现非预期的同学，可以拉取 NekoQuiz 的仓库，用老版本的代码构建 Docker 镜像。

具体操作如下：

```
$ git clone https://github.com/13m0n4de/neko-quiz
$ cd neko-quiz
$ git reset --hard 46ff2ee5319ea91cf1a6560af83698602d32635
$ docker-compose up
```
