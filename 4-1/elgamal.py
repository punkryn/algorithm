def powmod(a, b, p):
    res = 1
    b = int(b)
    while b:
        if b & 1:
            res = int(res * 1 * a % p)
            b -= 1
        else:
            a = int(a * 1 * 1 % p)
            b >>= 1
    return res

def generator(p):
    fact = []
    phi = p - 1
    n = phi

    i = 2
    while i * i <= n:
        if n % i == 0:
            fact.append(i)
            while n % i == 0:
                n /= i

        i += 1

    if n > 1:
        fact.append(n)

    for res in range(2, p + 1):
        ok = True
        j = 0
        while (j < len(fact)) and ok:
            ok &= powmod(res, phi / fact[j], p) != 1
            j += 1

        if ok:
            return res

    return -1

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def elgamal_encryption(e1, e2, p, P):
    r = 4
    c1 = (e1 ** r) % p
    c2 = (P * (e2 ** r)) % 11

    return (c1, c2)

def elgamal_decryption(d, p, ciphertext):
    c1, c2 = ciphertext

    P = (c2 * modinv(c1 ** d, p)) % p

    return P

Plaintext = 7
p = 11
e1 = generator(p)
d = 3
e2 = e1 ** d

Ciphertext = elgamal_encryption(e1, e2, p, Plaintext)
Plaintext_ = elgamal_decryption(d, p, Ciphertext)

print('e1:', e1)
print('Ciphertext:', Ciphertext)
print('Plaintext:', Plaintext_)
