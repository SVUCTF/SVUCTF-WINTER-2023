# nc

- 作者：13m0n4de
- 参考：-
- 难度：Baby/Trivial/Easy/Normal/Medium/Hard/Expert/Insane
- 分类：Pwn
- 镜像：[svuctf-winter-2023/nc](https://ghcr.io/svuctf/svuctf-winter-2023/nc:latest)
- 端口：70

## 题目描述

在命令不回显的一分钟里，我急了，手机电脑全砸了，别人说我急了好像真的恼羞成怒，躲在网络背后的我仿佛被看穿了，这种感觉很难受，短短急了两字我伪装出来的坚强和强颜欢笑全部崩塌，成了一个小丑，不想故作坚强了，玩心态我输得什么都不剩

## 题目解析

```
cat /flag 1>&0
```
