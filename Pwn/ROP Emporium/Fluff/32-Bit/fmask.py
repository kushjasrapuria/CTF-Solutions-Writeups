from pwn import *

hardcodedvalue = 0xb0bababa
tstring = 'flag.txt'
fullmask = []

for c in tstring:
        mask = ""
        hcount = 0
        tcount = 0

        hardcorededbits = bits(hardcodedvalue, endian='little')
        sbits = bits(u8(c), endian='little')

        while tcount < len(sbits) - 1:
                if hardcorededbits[hcount] == sbits[tcount]:
                        mask += "1"
                        tcount += 1
                else:
                        mask += "0"
                hcount += 1

        mask += ("0" * (16-len(mask)))
        mask = ''.join(reversed(mask))
        fullmask.append(mask)

hexmask = [hex(u16(unbits((i)), endian='big')) for i in fullmask]
print('In hex : ', '[%s]' % ' , '.join(map(str, hexmask)))
