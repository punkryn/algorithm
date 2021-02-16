# 2
# 5 6
# 0 0 1 0

# https://www.acmicpc.net/problem/14888

from itertools import permutations
from itertools import product

n = int(input())

fomula = list(map(int, input().split()))

op = list(map(int, input().split()))

oplist = []
for i, num in enumerate(op):
    for j in range(num):
        oplist.append(i)

#print(oplist)

max_value = 0
min_value = int(1e9)
#print(oplist)
for p in product(oplist, repeat=(n - 1)):
    #print(p)
    result = fomula[0]
    for i in range(1, n):
        if p[i - 1] == 0:
            result += fomula[i]
        elif p[i - 1] == 1:
            result -= fomula[i]
        elif p[i - 1] == 2:
            result *= fomula[i]
        else:
            if result >= 0:
                result //= fomula[i]
            else:
                result *= (-1)
                result //= fomula[i]
                result *= (-1)

    if max_value < result:
        #print('p', p)
        max_value = result
    if min_value > result:
        min_value = result

print(max_value)
print(min_value)