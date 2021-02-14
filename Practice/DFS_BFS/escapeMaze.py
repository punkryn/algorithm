from collections import deque

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    global count
    while queue:
        count += 1
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if matrix[nx][ny] == 0:
                continue

            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                for a in range(n):
                    for b in range(m):
                        print(matrix[a][b], end=' ')
                    print()
                print()
                queue.append((nx, ny))

            # if nx == n-1 and ny == m-1:
            #     print(1)
            #     return matrix[n-1][m-1]

    return matrix[n-1][m-1]
print(bfs(0, 0))
print(count)
