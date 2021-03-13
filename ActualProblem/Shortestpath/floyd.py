# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4

# https://www.acmicpc.net/problem/11404

INF = int(1e9)

n = int(input())
m = int(input())

matrix = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            matrix[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if matrix[a][b] > c:
        matrix[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            #if a != b:
            matrix[a][b] = min(matrix[a][b], matrix[a][k] + matrix[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if matrix[i][j] == INF:
            print(0, end=' ')
        else:
            print(matrix[i][j], end=' ')
    print()

