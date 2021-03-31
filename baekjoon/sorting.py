# https://www.acmicpc.net/problem/10989

# 10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7

from sys import stdin

n = int(input())

c = [0] * 10001
maxv = 0

for i in range(n):
    num = int(stdin.readline())
    c[num] += 1
    if num > maxv:
        maxv = num

for i in range(maxv + 1):
    for j in range(c[i]):
        print(i)