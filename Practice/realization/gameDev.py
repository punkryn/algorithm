from sys import stdin
N, M = map(int, input().split())

A, B, d = map(int, input().split())

matrix = [stdin.readline().split() for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

way = [[A, B]]
count = 1
directCount = 0
while True:
    print(A, B, directCount, d)

    if directCount == 4:
        if matrix[A - dx[d]][B - dy[d]] == '1':
            break
        else:
            A -= dx[d]
            B -= dy[d]
            directCount = 0
            continue

    d = d - 1 if d > 0 else 3

    try:
        if matrix[A + dx[d]][B + dy[d]] == '0' and [A + dx[d], B + dy[d]] not in way:
            A += dx[d]
            B += dy[d]
            count += 1
            #matrix[A][B] = '1'
            way.append([A, B])
            directCount = 0
        else:
            directCount += 1
            continue
    except IndexError:
        directCount += 1

print(count)

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x,y,direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:

    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)