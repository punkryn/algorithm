# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2

# https://www.acmicpc.net/problem/18405

from collections import deque

n, k = map(int, input().split())

tube = [list(map(int, input().split())) for _ in range(n)]

s, x, y = map(int, input().split())
x -= 1
y -= 1

virus_pos = []
for i in range(n):
    for j in range(n):
        if tube[i][j] != 0:
            virus_pos.append((tube[i][j], i, j, 0))

virus_pos.sort()

# up down left right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(tube, virus_pos, s):
    while virus_pos:
        value, x, y, count = virus_pos.pop(0)
        if count == s:
            return tube
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if tube[nx][ny] == 0:
                tube[nx][ny] = value
                virus_pos.append((value, nx, ny, count + 1))

bfs(tube, virus_pos, s)
print(tube[x][y])