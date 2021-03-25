# https://www.acmicpc.net/problem/7562

# 3
# 8
# 0 0
# 7 0
# 100
# 0 0
# 30 50
# 10
# 1 1
# 1 1

from collections import deque

def bfs(start, dest):
    q = deque()
    q.append((start, 0))
    visited[start[0]][start[1]] = 0

    while q:
        (x, y), cost = q.popleft()

        if x == dest[0] and y == dest[1]:
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = cost + 1
                    q.append(((nx, ny), cost + 1))



#   0  7
# 1      6
# 2      5
#   3  4
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

for _ in range(int(input())):
    l = int(input())
    now = list(map(int, input().split()))
    dest = list(map(int, input().split()))

    visited = [[0] * l for _ in range(l)]

    bfs(now, dest)

    print(visited[dest[0]][dest[1]])
