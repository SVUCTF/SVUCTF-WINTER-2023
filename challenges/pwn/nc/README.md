# nc

- 作者：13m0n4de
- 参考：-
- 难度：Easy
- 分类：Pwn
- 镜像：[svuctf-winter-2023/nc](https://ghcr.io/svuctf/svuctf-winter-2023/nc:latest)
- 端口：70

## 题目描述

在命令不回显的一分钟里，我急了，手机电脑全砸了，别人说我急了好像真的恼羞成怒，躲在网络背后的我仿佛被看穿了，这种感觉很难受，短短急了两字我伪装出来的坚强和强颜欢笑全部崩塌，成了一个小丑，不想故作坚强了，玩心态我输得什么都不剩

## 题目解析

```
....................................
[command] sh 1>/dev/null 2>/dev/null
....................................
```

根据回显信息，判断出我们已经执行了 `sh` ，但标准输出和标准错误都被重定向到了 `/dev/null` 。

`/dev/null` 是一个特殊的设备文件，任何写入到它的数据都会被丢弃。

有关重定向和文件描述符的知识请自行搜索。

我们可以把标准输出给重定向到标准输入中，这样命令的结果就会打印到终端里去：

```
cat /flag 1>&0
```

当然你也可以先获取一个有回显的 Shell

```
sh 1>&0 2>&0
```

需要注意的是，题目运行在 chroot 下，没有创建 `/dev/stdout` 、`/dev/fd/1` 等文件，不能把输出重定向到它们。
