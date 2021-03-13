# 3
# 0 0 0
# 0 0 0
# 0 9 0

# https://www.acmicpc.net/problem/16236

from collections import deque


def findEatable(space, shark_pos, shark):
    q = deque()

    tmpx, tmpy = shark_pos

    eatableList = []

    dis = 0

    q.append((tmpx, tmpy, dis))

    visited = [[False] * n for _ in range(n)]
    pre = int(1e9)
    while q:
        x, y, dis = q.popleft()

        # print(x, y, dis, pre)
        # for a in range(n):
        #     for b in range(n):
        #         print(visited[a][b], end=' ')
        #     print()
        # print()

        if dis == pre:
            break

        dis += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if space[nx][ny] > shark or visited[nx][ny]:
                    continue

                elif 0 < space[nx][ny] < shark and not visited[nx][ny]:
                    if pre == int(1e9):
                        pre = dis
                    eatableList.append((nx, ny, dis))
                    q.append((nx, ny, dis))
                else:
                    q.append((nx, ny, dis))

                visited[nx][ny] = True

    #print(pre)
    return eatableList

n = int(input())

space = [list(map(int, input().split())) for _ in range(n)]

shark = 2

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

shark_pos = 0

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark_pos = (i, j)
            break

time = 0
quanty = 0
space[shark_pos[0]][shark_pos[1]] = 0
while True:
    eatable = findEatable(space, shark_pos, shark)
    # print(eatable)
    if len(eatable) == 1:
        #print(eatable)
        x, y, dis = eatable[0]
        time += dis
        space[x][y] = 0
        quanty += 1
        shark_pos = (x, y)
    elif len(eatable) > 1:
        eatable.sort(key=lambda x: (x[0], x[1]))
        #print(eatable)
        x, y, dis = eatable[0]
        time += dis
        space[x][y] = 0
        quanty += 1
        shark_pos = (x, y)
    else:
        break

    # for a in range(n):
    #     for b in range(n):
    #         print(space[a][b], end=' ')
    #     print()
    # print()

    if quanty == shark:
        shark += 1
        quanty = 0

print(time)