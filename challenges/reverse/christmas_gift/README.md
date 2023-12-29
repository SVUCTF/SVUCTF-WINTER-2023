# 圣诞礼物

- 作者：13m0n4de
- 参考：-
- 难度：Baby/Trivial/Easy/Normal/Medium/Hard/Expert/Insane
- 分类：Reverse
- 镜像：-
- 端口：-

## 题目描述

不要把礼物包的那么严实啊喂

## 题目解析

一个由 Racket 编写的程序，它是一门 Lisp 方言。

你可以看到它的代码和平常熟知的代码形式很不同，只有小括号（Racket 添加了意义完全一样的中括号），函数调用也不是 `func(arg1, arg2)` 而是 `(func arg1 arg2)`，这种“奇怪”的形式叫做 S 表达式，它是 Lisp 语言的特色，更多可以自行了解。

```racket
#lang racket

(define (wrap-gift gift)
  (define (merry-coding index len)
    (when (< index len)
      (let* ([char-code (char->integer (string-ref gift index))]
             [encoded-char (cond [(and (>= char-code 97) (<= char-code 122)) (- char-code 32)]
                                 [(and (>= char-code 65) (<= char-code 90)) (+ char-code 32)]
                                 [else char-code])]
             [encoded-char (bitwise-xor index encoded-char)])
        (printf "#~a" encoded-char)
        (merry-coding (+ index 1) len))))
  (merry-coding 0 (string-length gift))
  (newline))

(define (christmas-greetings)
  (let ([gift "flag{???????????????????????????}"])
    (wrap-gift gift)))

(christmas-greetings)
```

程序定义了 `wrap-gift` 函数，它有一个参数 `gift`。

在函数中定义了另一个辅助函数 `merry-coding`，它传入一个索引值 `index` 和一个长度 `len` 。

当 `index` 小于 `len` 的时候，会执行一个 `let` 语句。

在 `let` 语句中：

- `char-code` 被赋值为 `gift` 字符串中索引为 `index` 的字符的 ASCII 码值，使用 `char->integer` 函数进行转换。
- `encoded-char` 被计算为根据字符的 ASCII 码值进行变换。其实就是大小写互换了。
- `encoded-char` 被再次赋值，这次使用了按位异或运算符 `bitwise-xor`，将索引 `index` 和之前计算得到的 `encoded-char` 进行异或。
- 使用 `printf` 函数输出一个格式化的字符串，其中 `#~a` 表示输出类似 `#100` 格式的字符串，对应 [gift.txt](./attachments/gift.txt) 中的内容。
- 递归调用 `merry-coding` 函数，传入更新后的索引 `(+ index 1)` 和原始的长度 `len`。

这些你都可以在 [Racket 的官方文档](https://docs.racket-lang.org) 中查到。

解密脚本 [solve.py](./writeup/solve.py) ：

```python
gift = "#70#77#67#68#127#86#50#105#124#104#45#120#83#74#66#73#100#78#116#35#70#74#113#120#119#125#69#80#45#121#109#98"
flag = ""

for index, char in enumerate(gift.split("#")[1:]):
    char_code = int(char)
    char_code ^= index
    flag += chr(char_code).swapcase()

print(flag)
# flag{s4NTA'S_glfT_F0r_GOOD_k1DS}
```
