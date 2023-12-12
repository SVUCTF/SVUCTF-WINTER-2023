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
