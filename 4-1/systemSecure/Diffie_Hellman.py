g = 7
p = 23

x = 3
R1 = g ** x % p

y = 6
R2 = g ** y % p

aK = R2 ** x % p
bK = R1 ** y % p

print("Alice K", aK)
print("Bob K", bK)
print(g ** (x * y) % p)