# 签到

- 作者：Cee
- 参考：-
- 难度：Easy
- 分类：Crypto
- 镜像：-
- 端口：-

## 题目描述

圣诞夜到了，学长没什么好送的，送你们一个flag吧~

## 题目解析

首先拿到题目

```
VZu9GZsxWZXt3ZhxmZ==9NXaoR3Xzl2XzlGa09
```

进行翻转一下

```
90aGlzX2lzX3RoaXN9==ZmxhZ3tXZWxsZG9uZV
```

中间有两个=号 转换一个顺序

```
ZmxhZ3tXZWxsZG9uZV90aGlzX2lzX3RoaXN9==
```

使用base64

```
flag{Welldone_this_is_this}
```

这可简单了啊
