from math import gcd

data = bytearray(open('encrypted.bin', 'rb').read())
m = 256

def affine(n, a, b):
    return (a*n + b) % m

for a in range(m):
    if gcd(a, m) != 1: # This is a necessary condition for a
        continue
    for b in range(m):
        new = [affine(data[0],a,b), affine(data[1],a,b)] # decode just the first 2 bytes
        if new == [37, 80]: # pdf magic bytes
            print("possible pdf:",a,b)

# decode the whole file now using the a and b we found
pdf = bytearray([affine(b,153,96) for b in list(data)]) 
open('flag.pdf','wb').write(pdf)
