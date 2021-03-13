# 빈 공간의 인덱스를 리스트에 저장하여 3개 조합을 만든다.
# 조합을 하나 하나 꺼내 해당 위치에 벽을 세우고 바이러스를 이동시키고
# 이동시킨 후 0의 개수를 세고 이 중 최댓값을 출력한다.

# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

# https://www.acmicpc.net/problem/14502

from itertools import combinations

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

virus_pos = []
wall_pos = []
blank_pos = []

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            virus_pos.append((i, j))
        elif matrix[i][j] == 1:
            wall_pos.append((i, j))
        else:
            blank_pos.append((i, j))
# up down left right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(virus, matrix_copy):
    stack = []
    stack.append(virus)
    #size = len(stack)
    while stack:
        #size = len(stack) if len(stack) > size else size
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue
            #print('nx, ny', nx, ny)
            if matrix_copy[nx][ny] == 0:
                matrix_copy[nx][ny] = 2
                stack.append((nx, ny))
            elif matrix_copy[nx][ny] == 1:
                continue
            else:
                continue
    #print(size)
    return matrix_copy

comb = combinations(blank_pos, 3)
max_value = 0
mat = []
for com in comb:
    #print(c)
    matrix_copy = [[0] * m for _ in range(n)]
    #print(matrix_copy)
    result = 0

    for virus in virus_pos:
        a, b = virus
        matrix_copy[a][b] = 2

    for wall in wall_pos:
        a, b = wall
        matrix_copy[a][b] = 1

    for co in com:
        a, b = co
        matrix_copy[a][b] = 1

    for virus in virus_pos:
        mat = dfs(virus, matrix_copy)

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                result += 1

    if max_value < result:
        max_value = result
        # for i in range(n):
        #     for j in range(m):
        #         print(mat[i][j], end='')
        #     print()
        # print()

print(max_value)