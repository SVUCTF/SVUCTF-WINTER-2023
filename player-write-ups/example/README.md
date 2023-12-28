# SVUCTF-WINTER-2023 WP from 选手名字

这是一个简单的题解示例。

题解文件夹请不要以中文命名，整个文档命名为 `README.md`，以 Markdown 格式编写。

内容格式没有任何限制，但请保证至少易于阅读。

附件过多可以新建一个文件夹，例如 `images/` 或者 `scripts/` 或者 `files/` ，注意附件不宜过大。

假如你的名字是 `13m0n4de`，你的目录结构可能是：

```
player-write-ups/
└── 13m0n4de
    ├── images
    │   └── poster-crt.png
    └── README.md
```

你可以在这里简单介绍自己，或是发表对整个比赛的感想。

## 题目名

在这里你可以介绍做题的完整过程。

可以附上代码：

```asm
.global _start

.section .data
greeting: .asciz "Welcome to SVUCTF Winter 2023!\n"

.section .text
_start:
    li a0, 1
    la a1, greeting
    li a2, 31
    li a7, 64
    ecall

    li a0, 0
    li a7, 93
    ecall
```

或是附上图片：

![poster-crt](./images/poster-crt.png)

## 第二个题目名

这里同上
