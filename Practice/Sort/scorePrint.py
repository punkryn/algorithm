from sys import stdin

n = int(input())

matrix = [stdin.readline().split() for _ in range(n)]

matrix.sort(key=lambda k: k[1])

for item in matrix:
    print(item[0], end=' ')