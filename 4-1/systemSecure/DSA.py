def egcd(a, b):
    #print(a, b)
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        #print(g, y, x)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    #print(g, x, y)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

print(modinv(15, 442))
print((2**320)%3119)

p = 8081
q = 101
e0 = 3
e1 = e0 ** ((p - 1) // q) % p
print("e1:", e1)
d = 61
e2 = e1 ** d % p
print("e2:", e2)
hM = 5000
r = 61

S1 = ((e1 ** r) % p) % q
print("S1:", S1)
S2 = ((hM + d * S1) * modinv(r, q)) % q
print("S2:", S2)

S2_ = modinv(S2, q)
print("S2_:", S2_)

V = (((e1 ** (hM * S2_)) * (e2 ** (S1 * S2_))) % p) % q
print("V:", V)