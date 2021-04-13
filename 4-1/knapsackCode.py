def knapsackSum(x, a):
    s = 0
    for i in range(len(a)):
        s += (x[i] * a[i])
    return s

def inv_knapsackSum(s, a):
    x = []
    for i in range(len(a) - 1, -1, -1):
        if a[i] <= s:
            x.append(1)
            s %= a[i]
        else:
            x.append(0)
    x.reverse()
    return x

def permute(t):
    a = [0] * len(t)
    for i, n in enumerate(t):
        a[i] = t[permute_table[i] - 1]
    return a

def uclid(r, n):
    u2_, v2_ = 1, 0
    u1_, v1_ = 0, 1
    u, v = 0, 0

    r1 = n * u2_ + r * v2_
    r2 = n * u1_ + r * v1_

    while r2 > 1:
        u, v = u2_ - (u1_ * (r1 // r2)), v2_ - (v1_ * (r1 // r2))
        u2_, v2_ = u1_, v1_
        u1_, v1_ = u, v

        r1 = r2
        r2 = n * u + r * v
    return v

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        print('g, y, x', g, y, x)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    print('1', g,x,y)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

p = 397
q = 401
n = p * q
pin = (p-1)*(q-1)
e = 343
d = modinv(e, pin)
print(d)

b = [7, 11, 19, 39, 79, 157, 313]
n = 900
r = 37
permute_table = [4, 2, 5, 3, 1, 7, 6]
t = [(r * x) % n for x in b]
print('t:', t)
a = permute(t)
print('a:', a)

x = [1, 1, 0, 0, 1, 1, 1]
s = knapsackSum(a, x)
print('s:', s)

r_ = uclid(r, n)
print('ttt', modinv(r, n))
print('r_:', r_)
s_ = s * r_ % n
print('s_:', s_)
x_ = inv_knapsackSum(s_, b)
print('x_:', x_)

x = permute(x_)
print('x:', x)