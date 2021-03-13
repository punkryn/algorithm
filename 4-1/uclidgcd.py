def gcd(a, b):
    if a > b:
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    else:
        if a == 0:
            return b
        else:
            return gcd(a, b % a)

print(gcd(1071, 342))
print(gcd(342, 1071))

