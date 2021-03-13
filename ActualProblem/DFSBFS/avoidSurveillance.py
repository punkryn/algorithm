# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X

# https://www.acmicpc.net/problem/18428

from itertools import combinations

def dfs(teacher, room, d):
    x, y = teacher

    for i in range(4):
        if i != d:
            continue
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < n):
            return

        if room[nx][ny] == 'X':
            dfs((nx, ny), room, i)
        elif room[nx][ny] == 'S':
            room[nx][ny] = 'W'
            dfs((nx, ny), room, i)
        elif room[nx][ny] == 'T':
            return
        else:
            return



n = int(input())

room = [list(input().split()) for _ in range(n)]

blank_pos = []
teacher_pos = []
student_pos = []

for i in range(n):
    for j in range(n):
        if room[i][j] == 'X':
            blank_pos.append((i, j))
        elif room[i][j] == 'S':
            student_pos.append((i, j))
        else:
            teacher_pos.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sw = False
for blank in combinations(blank_pos, 3):
    tmp = [[0] * n for _ in range(n)]
    for b in blank_pos:
        x, y = b
        tmp[x][y] = 'X'
    for o in blank:
        x, y = o
        tmp[x][y] = 'O'
    for t in teacher_pos:
        x, y = t
        tmp[x][y] = 'T'
    for s in student_pos:
        x, y = s
        tmp[x][y] = 'S'

    for teacher in teacher_pos:
        for i in range(4):
            dfs(teacher, tmp, i)

    # for a in range(n):
    #     for b in range(n):
    #         print(tmp[a][b], end=' ')
    #     print()
    # print()

    aaa = []
    for student in student_pos:
        x, y = student
        if tmp[x][y] == 'W':
            aaa.append('W')
    #print('aaa', aaa)
    if not aaa:
        sw = True
        break

if sw:
    print('YES')
else:
    print('NO')