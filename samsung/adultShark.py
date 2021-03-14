# 5 4 4
# 0 0 0 0 3
# 0 2 0 0 0
# 1 0 0 0 4
# 0 0 0 0 0
# 0 0 0 0 0
# 4 4 3 1
# 2 3 1 4
# 4 1 2 3
# 3 4 2 1
# 4 3 1 2
# 2 4 3 1
# 2 1 3 4
# 3 4 1 2
# 4 1 2 3
# 4 3 2 1
# 1 4 3 2
# 1 3 2 4
# 3 2 1 4
# 3 4 1 2
# 3 2 4 1
# 1 4 2 3
# 1 4 2 3
#
# https://www.acmicpc.net/problem/19237

# 이동 룰
# 1. 무취
# 2. 자신의 냄새
# 3. 특수한 우선 순위

def find_shark_pos(matrix, m):
    pos = []
    for k in range(1, m + 1):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == k:
                    pos.append((i, j))

    return pos

def smell_down(smell):
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1

                if smell[i][j][1] == 0:
                    smell[i][j][0] = -1

def show_matrix(matrix, smell):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')

        print(end='\t')

        for j in range(n):
            print(smell[i][j], end=' ')
        print()
    print()

n, m, k = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

smell = []
for i in range(n):
    smell.append([])
    for j in range(n):
        smell[i].append([-1, 0])

#print(smell)

shark_direction = list(map(int, input().split()))
# shark_direction.insert(0, 0)

order = [[list(map(int, input().split())) for _ in range(4)] for __ in range(m)]

# order.insert(0, [])
#print(order)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

shark_pos = find_shark_pos(matrix, m)
shark_num = len(shark_pos)
#print(shark_pos)
time = 0

while shark_num > 1:
    time += 1
    if time > 1000:
        time = -1
        break

    #print(shark_pos)
    #show_matrix(matrix, smell)

    # 현재 위치에 냄새 설정
    for i, pos in enumerate(shark_pos):
        x, y = pos
        if x == -1 and y == -1:
            continue
        smell[x][y] = [i, k]

    #show_matrix(matrix, smell)

    # 이동 가능한 위치 찾기
    tmplist = []
    for i, pos in enumerate(shark_pos):
        x, y = pos
        if x == -1 and y == -1:
            continue

        tmp = []
        for d in order[i][shark_direction[i]-1]:
            nx = x + dx[d - 1]
            ny = y + dy[d - 1]

            if 0 <= nx < n and 0 <= ny < n:
                if smell[nx][ny] == [-1, 0]:
                    tmp.append((nx, ny, d))
                    break

        if not tmp:
            for d in order[i][shark_direction[i]-1]:
                nx = x + dx[d - 1]
                ny = y + dy[d - 1]

                if 0 <= nx < n and 0 <= ny < n:
                    if smell[nx][ny][0] == i:
                        tmp.append((nx, ny, d))
                        break

        tmplist.append([(x, y), tmp[0], i])
        # if tmp:
        #     nx, ny, d = tmp[0]
        #     if matrix[x][y] == i + 1:
        #         matrix[x][y] = 0
        #     if matrix[nx][ny] != 0 and matrix[nx][ny] < i + 1:
        #         shark_num -= 1
        #         shark_pos[i] = (-1, -1)
        #     else:
        #         matrix[nx][ny] = i + 1
        #         shark_pos[i] = (nx, ny)
        #
        #     shark_direction[i] = d

    for item in tmplist:
        x, y = item[0]
        matrix[x][y] = 0

    for item in tmplist:
        nx, ny, d = item[1]
        i = item[2]

        if matrix[nx][ny] != 0 and matrix[nx][ny] < i + 1:
            shark_num -= 1
            shark_pos[i] = (-1, -1)
        else:
            matrix[nx][ny] = i + 1
            shark_pos[i] = (nx, ny)

        shark_direction[i] = d

    smell_down(smell)

print(time)