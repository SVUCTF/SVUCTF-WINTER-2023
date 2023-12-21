# solver

- 作者：pn1fg
- 参考：-
- 难度：Baby/Trivial/Easy/Normal/Medium/Hard/Expert/Insane
- 分类：Reverse
- 镜像：-
- 端口：-

## 题目描述

@pn1fg：「唉，苦恼 Reverse 出什么题目...」\
@pn1fg：「我打算用 Rust 写一个，练练手。」\
@13m0n4de：「行呗，写。」\
@pn1fg：「奋斗中，一天、两天...」\
@13m0n4de：「夜深中... `RustDesk` 共享桌面，开始补救...」\
@pn1fg：「摸鱼中...」\
@13m0n4de：「已经越写越魔幻了，难绷。」\
@13m0n4de：「`flag_checker` 里准备放啥？」\
@pn1fg：「XOR？TEA？Z3？看心情吧！」\
@13m0n4de：「...」\
@13m0n4de：「Pwn？」\
@pn1fg：「走！」

## 题目解析

- 源码：[main.rs](build/main.rs)
- 考点：Rust 逆向，XOR，Z3 约束求解

### 查看文件信息

查壳：

```
$ diec solver
ELF64
    Operation system: Unix(-)[DYN AMD64-64]
    Library: GLIBC(2.34)[DYN AMD64-64]
    Compiler: Rust(-)[DYN AMD64-64]
    Compiler: gcc(3.X)[DYN AMD64-64]
```

64位 ELF 可执行文件

反编译文件

- 查看`main`函数

```rust
void dbg.main(void)
{
  uchar auStack128 [48];
  ulong uStack80;
  ulong uStack72;
  ulong uStack64;
  ulong uStack56;
  ulong uStack48;
  ulong uStack40;
  ulong uStack32;
  ulong uStack24;
  ulong uStack16;
  ulong uStack8;

  void main();
  dbg.banner();
  dbg.core::fmt::Arguments::new_const::hb3b1527f2e3063d8(auStack128, 0x5d230, 1);
  (**0x5fe28)(auStack128);
  dbg.read_numbers(&uStack80);
  uStack40 = uStack80;
  uStack32 = uStack72;
  uStack24 = uStack64;
  uStack16 = uStack56;
  uStack8 = uStack48;
  dbg.flag_checker(uStack80, uStack72, uStack64, uStack56, uStack48);
  return;
} 
```

`main` 函数中接收了五个整形值，然后调用了 `flag_checker` 函数

- 查看 `flag_checker` 函数

```rust
void dbg.flag_checker(uint64_t arg1, uint64_t arg2, uint64_t arg3, uint64_t arg4, uint64_t arg5)

{
    uint64_t uStack528;
    uint64_t uStack520;
    uint64_t uStack512;
    uint64_t uStack504;
    uint64_t uStack496;
    ulong uStack488;
    ulong uStack480;
    ulong uStack472;
    ulong uStack464;
    ulong uStack456;
    ulong uStack448;
    uchar auStack440 [48];
    uint64_t *puStack392;
    code *pcStack384;
    uint64_t *puStack376;
    code *pcStack368;
    uint64_t *puStack360;
    code *pcStack352;
    uint64_t *puStack344;
    code *pcStack336;
    uint64_t *puStack328;
    code *pcStack320;
    uchar auStack312 [48];
    ulong *puStack264;
    code *pcStack256;
    uchar auStack248 [48];
    ulong *puStack200;
    code *pcStack192;
    ulong *puStack184;
    code *pcStack176;
    uint64_t *puStack168;
    code *pcStack160;
    uint64_t *puStack152;
    code *pcStack144;
    uint64_t *puStack136;
    code *pcStack128;
    uint64_t *puStack120;
    code *pcStack112;
    uint64_t *puStack104;
    code *pcStack96;
    uint64_t *puStack88;
    code *pcStack80;
    uint64_t *puStack72;
    code *pcStack64;
    uint64_t *puStack56;
    code *pcStack48;
    uint64_t *puStack40;
    code *pcStack32;
    uint64_t *puStack24;
    code *pcStack16;

    // void flag_checker(i64 a,i64 b,i64 c,i64 d,i64 e);
    puStack392 = &uStack528;
    pcStack16 = sym.core::fmt::num::imp::__impl_core::fmt::Display_for_i64_::fmt::h7d1a869ab67fdf56;
    pcStack32 = sym.core::fmt::num::imp::__impl_core::fmt::Display_for_i64_::fmt::h7d1a869ab67fdf56;
    puStack376 = &uStack520;
    pcStack48 = sym.core::fmt::num::imp::__impl_core::fmt::Display_for_i64_::fmt::h7d1a869ab67fdf56;
    pcStack64 = sym.core::fmt::num::imp::__impl_core::fmt::Display_for_i64_::fmt::h7d1a869ab67fdf56;
    puStack360 = &uStack512;
    pcStack80 = sym.core::fmt::num::imp::__impl_core::fmt::Display_for_i64_::fmt::h7d1a869ab67fdf56;
    pcStack96 = sym.core::fmt::num::imp::__impl_core::fmt::Display_for_i64_::fmt::h7d1a869ab67fdf56;
    puStack344 = &uStack504;
    pcStack112 = sym.core::fmt::num::imp::__impl_core::fmt::Display_for_i64_::fmt::h7d1a869ab67fdf56;
    pcStack128 = sym.core::fmt::num::imp::__impl_core::fmt::Display_for_i64_::fmt::h7d1a869ab67fdf56;
    puStack328 = &uStack496;
    pcStack144 = sym.core::fmt::num::imp::__impl_core::fmt::Display_for_i64_::fmt::h7d1a869ab67fdf56;
    pcStack160 = sym.core::fmt::num::imp::__impl_core::fmt::Display_for_i64_::fmt::h7d1a869ab67fdf56;
    pcStack384 = sym.core::fmt::num::imp::__impl_core::fmt::Display_for_i64_::fmt::h7d1a869ab67fdf56;
    pcStack368 = sym.core::fmt::num::imp::__impl_core::fmt::Display_for_i64_::fmt::h7d1a869ab67fdf56;
    pcStack352 = sym.core::fmt::num::imp::__impl_core::fmt::Display_for_i64_::fmt::h7d1a869ab67fdf56;
    pcStack336 = sym.core::fmt::num::imp::__impl_core::fmt::Display_for_i64_::fmt::h7d1a869ab67fdf56;
    pcStack320 = sym.core::fmt::num::imp::__impl_core::fmt::Display_for_i64_::fmt::h7d1a869ab67fdf56;
    uStack528 = arg1;
    uStack520 = arg2;
    uStack512 = arg3;
    uStack504 = arg4;
    uStack496 = arg5;
    puStack168 = puStack328;
    puStack152 = puStack328;
    puStack136 = puStack344;
    puStack120 = puStack344;
    puStack104 = puStack360;
    puStack88 = puStack360;
    puStack72 = puStack376;
    puStack56 = puStack376;
    puStack40 = puStack392;
    puStack24 = puStack392;
    dbg.core::fmt::Arguments::new_v1::h85b002cb44949918(auStack440, 0x5d120, 6, &puStack392, 5);
    dbg.format(&uStack464, auStack440);
    uStack488 = uStack464;
    uStack480 = uStack456;
    uStack472 = uStack448;
    uStack528 = uStack528 ^ 0xfda;
    uStack520 = uStack520 ^ 0xedb;
    uStack512 = uStack512 ^ 0xddc;
    uStack504 = uStack504 ^ 0xcdd;
    uStack496 = uStack496 ^ 0xbde;
    if ((((uStack528 * 0xfdb55 + uStack520 * 0x8048e + uStack512 * 0x7f880 + uStack504 * -0xa854 + uStack496 * 0x7f8048
           == 0x6b659a58b) &&
         (uStack528 * 0xfef55 + uStack520 * 0x8cd8e + uStack512 * 0x7f450 + uStack504 * -0xfa54 + uStack496 * 0x7f548 ==
          0x1e3a8d33b)) &&
        (uStack528 * 0xace55 + uStack520 * 0x34f8e + uStack512 * 0xa340 + uStack504 * -0xf354 + uStack496 * 0x7fed8 ==
         0xfbc657eb)) &&
       ((uStack528 * 0xfdc55 + uStack520 * 0x4888e + uStack512 * 0x7fe20 + uStack504 * -0xa054 + uStack496 * 0xf548 ==
         0x1683d53eb &&
        (uStack528 * 0xaeb55 + uStack520 * 0x8048e + uStack512 * 0x10a0e + uStack504 * -0xa0854 + uStack496 * 0xf0fe ==
         0x7a95e0d9)))) {
        puStack264 = &uStack488;
        pcStack176 = sym._alloc::string::String_as_core::fmt::Display_::fmt::h2c0e06606cbbc0fb;
        pcStack192 = sym._alloc::string::String_as_core::fmt::Display_::fmt::h2c0e06606cbbc0fb;
        pcStack256 = sym._alloc::string::String_as_core::fmt::Display_::fmt::h2c0e06606cbbc0fb;
        puStack200 = puStack264;
        puStack184 = puStack264;
        dbg.core::fmt::Arguments::new_v1::h85b002cb44949918(auStack312, 0x5d180, 2, &puStack264, 1);
        (**0x5fe28)(auStack312);
    }
    else {
        dbg.core::fmt::Arguments::new_const::hb3b1527f2e3063d8(auStack248, 0x5d1a0, 1);
        (**0x5fe28)(auStack248);
    }
    dbg.drop_in_place<alloc::string::String>(&uStack488);
    return;
}
```

工具的问题，大家用 IDA 看的时候可能会舒服一点

`flag_checker` 函数中首先将我们输入的五个整形值进行了异或，然后在 `if/else` 条件判断语句中列出了类似于方程组的条件，分析到这本题的大致思路就是先利用 `z3 约束求解器` 解出五个整形值，随后进行异或即可

### 编写利用程序

```python
from z3 import *

a = Real('a')
b = Real('b')
c = Real('c')
d = Real('d')
e = Real('e')

s = Solver()

s.add(a * 0xfdb55 + b * 0x8048e + c * 0x7f880 - d * 0x0a854 + e * 0x7f8048 == 0x6b659a58b)
s.add(a * 0xfef55 + b * 0x8cd8e + c * 0x7f450 - d * 0x0fa54 + e * 0x7f548 == 0x1e3a8d33b)
s.add(a * 0xace55 + b * 0x34f8e + c * 0x0a340 - d * 0xf354 + e * 0x7fed8 == 0xfbc657eb)
s.add(a * 0xfdc55 + b * 0x4888e + c * 0x7fe20 - d * 0xa054 + e * 0xf548 == 0x1683d53eb)
s.add(a * 0xaeb55 + b * 0x8048e + c * 0x10a0e - d * 0xa0854 + e * 0x0f0fe == 0x7a95e0d9)

if s.check() == sat:
    result = s.model()
    print (result)
else:
    print (b'no result')

a = result[a].as_long() ^ 0xfda
b = result[b].as_long() ^ 0xedb
c = result[c].as_long() ^ 0xddc
d = result[d].as_long() ^ 0xcdd
e = result[e].as_long() ^ 0xbde

print("\nThese Five numbers:")
print("a =",a,"\nb =",b,"\nc =",c,"\nd =",d,"\ne =",e)
```

**注意类型的转换**
