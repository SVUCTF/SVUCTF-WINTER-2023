from random import randint
from datetime import datetime, timedelta


class Message:
    def __init__(self, text: str, time: str):
        self.text = text
        self.time = time


def init_messages():
    messages = []
    texts = [
        """
        记录以及分享冬季赛解题过程，每过一段时间就来这里更新一下，欢迎投稿。
        """,
        """
        猫娘问答<br>
        很经典的问答题，主要就是问，多问。<br>
        第一问去找校内参赛的学长学姐问就好了。<br>
        第二问也是同理，找到新生赛的出题人线下询问。<br>
        第三问比较简单，发一封邮件给 Hex-Rays 问一下。<br>
        第四问有点麻烦，需要联系 RFC ，由于 RFC 使用了鸽载互联网，得用鸽子寄给它们，要注意容易受到中间猫攻击。
        """,
        """
        蟹黄堡秘方<br>
        这题做了好久，思路是先去海之霸买一份海霸糊，用 IDA Pro 逆向工程出海霸糊的配方，然后倒过来就是蟹黄堡秘方了。
        """,
        """
        esrever<br>
        简单的逆向题，名字都是 reverse 倒过来了，反编译查看字符串，得到 Base64 编码的 Flag。
        """,
        """
        babyrop<br>
        百度搜索 ROP ，发现是早产婴儿视网膜病变，也对应了 baby 一词，询问了医学生朋友，终于做出这题了。
        """,
        """
        FlagServer<br>
        网页上的猫娘图片是 AI 生成的，下载下来分析参数，使用相同模型相同参数更换种子多试几次就能生成出 Flag 图片。
        """,
        """
        文件上传<br>
        简单的社工得知图片是《亲爱的热爱的》，抱着学习的心态去看，结果看了一天忘了做题。
        """,
        """
        CGI<br>
        RE 题不知道为什么会有容器，打开来什么也看不到，应该是出题人搞错了，反馈给他，结果他一直在笑，根本没停过。
        """,
    ]

    time = datetime(year=2023, month=1, day=1, hour=9, minute=0)

    for text in texts:
        time += timedelta(hours=randint(0, 3), minutes=randint(15, 60))
        messages.append(Message(text, time.strftime("%H:%M")))

    return messages
