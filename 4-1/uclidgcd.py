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

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o','p','q','r','s','t','u','v','w','x','y','z']
sen = 'iamastudentatkit'
key = 'kumohkumohkumohk'

phrase = []
for i, word in enumerate(sen):
    print(a.index(word) + a.index(key[i]))
    phrase.append(a[((a.index(word) + a.index(key[i])) % 26)])

print(''.join(phrase))