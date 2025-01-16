#!/usr/bin/env python3

from pwn import *

gs = '''
init-pwndbg
continue
'''

#context.log_level = 'debug'

def conn():
    if args.GDB:
        return gdb.debug([elf.path], gdbscript=gs)
    elif args.LOCAL:
        return process([elf.path])
    else:
        return remote("3a18a9f15ba39cf3.247ctf.com", 50348)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    for i in range(500):
        io.recvuntil(b'What is the answer to ')
        a = int(io.recvuntil(b' ').rstrip())
        #info(a)
        io.recvuntil(b' ')
        b = int(io.recvuntil(b'?')[:-1])
        #info(b)
        c = str(a+b)
        #info(c)
        info(i)
        payload = flat(c, b'\r\n')
        io.sendline(payload)

    io.interactive()

if __name__ == "__main__":
    main()
