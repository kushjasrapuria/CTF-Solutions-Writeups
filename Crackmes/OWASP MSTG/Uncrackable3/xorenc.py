# Python 2 script

encsecret = "1d0811130f1749150d0003195a1d1315080e5a0017081314".decode("hex")
xorkey = "pizzapizzapizzapizzapizz"

def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

secret = xor_strings(encsecret,xorkey)
print ("The secret is: " + secret)
