<div align="center">

# SVUCTF-WINTER-2023

本仓库用于存储和构建 SVUCTF-HELLOWORLD-2023 的题目镜像。

Powered by GZCTF and GZTime

![poster](assets/glitched_poster.png)

</div>

## 目录

项目结构遵循 GZCTF 规范。

```
.github/workflows/                      # Github Actions
    └── <category>.<name>.yml               # 每个题目的编译脚本
challenges/                             # 所有题目
    ├── web/                                # 题目分类
    │   ├── challenge1/                         # 题目
    │   │   ├── build/                              # 构建文件
    │   │   │   ├── Dockerfile
    │   │   │   └── more...
    │   │   ├── attachments/                        # 附件
    │   │   ├── writeup/                            # 题解文件    
    │   │   └── README.md                           # 题目信息（含题解文本）
    │   └── more...
    └── more...
```
