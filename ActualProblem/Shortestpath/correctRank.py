# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4

n, m = map(int, input().split())

INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    #graph[b][a] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF and graph[j][i] == INF:
            count += 1
            break


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print('x', end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

print(n - count)