# 变异凯撒

- 作者：Cee
- 参考：-
- 难度：Baby/Trivial/Easy/Normal/Medium/Hard/Expert/Insane
- 分类：Crypto
- 镜像：-
- 端口：-

## 题目描述

百度一下https://zh.wikipedia.org/zh-sg/%E5%87%B1%E6%92%92%E5%AF%86%E7%A2%BC

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
