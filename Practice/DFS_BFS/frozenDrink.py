from collections import deque

N, M = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input())))

#print(matrix)

visited = [[0] * M for _ in range(N)]

count = 0

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    for a in range(N):
        for b in range(M):
            print(matrix[a][b], end='')
        print(end='\n')
    print()

    if matrix[x][y] == 0:
        matrix[x][y] = 1

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            count += 1
print(count)