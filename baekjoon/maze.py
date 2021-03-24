# https://www.acmicpc.net/problem/2178

# 4 6
# 101111
# 101010
# 101011
# 111011

from collections import deque

def bfs(start):
    q = deque()
    q.append((start, 1))

    while q:
        (x, y), cost = q.popleft()
        if x == n-1 and y == m-1:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and maze[nx][ny] == '1':
                    q.append(((nx, ny), cost + 1))
                    visited[nx][ny] = cost + 1


n, m = map(int, input().split())

maze = [list((input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

start = (0, 0)

bfs(start)

print(visited[n-1][m-1])