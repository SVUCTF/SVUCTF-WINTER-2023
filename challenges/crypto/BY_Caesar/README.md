# 题目名

- 作者：Cee-YSKM
- 参考：SVUCTF-2023
- 难度：Baby/Trivial/Easy/Normal/Medium/Hard/Expert/Insane
- 分类：Crypto
- 镜像：-
- 端口：-

## 题目描述

一道逆向编译的题目

## 题目解析

```python
flag = ''
for i, char in enumerate('{ccdd329`;2:3/bc45+92d7//817+g2:`857_}ecjh'):
    code = ord(char)
    # code -= 5
    if (i + 1) % 2 != 0:
        code += 2
    else:
        code -= 2
    # code += 5
    flag += chr(code)

print(flag[::-1])
```

