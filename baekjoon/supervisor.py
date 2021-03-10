# https://www.acmicpc.net/problem/13458
# 1
# 1
# 1 1

import math

n = int(input())

a = list(map(int, input().split()))

b, c = map(int, input().split())

result = 0
for item in a:
    if item - b > 0:
        result += 1
        #print(math.ceil((item - b) / c))
        result += math.ceil((item - b) / c)
    else:
        result += 1

print(result)