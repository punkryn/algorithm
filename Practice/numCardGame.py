from sys import stdin

N, M = map(int, input().split())

matrix = [stdin.readline().split() for _ in range(N)]

print(matrix)



MAX = 0
for i in range(N):
    for n in matrix[i]:
        MIN = int(min(matrix[i]))
        if MAX < MIN:
            MAX = MIN

print(MAX)

