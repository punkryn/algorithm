# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# https://www.acmicpc.net/problem/3190

# 0, 0에서 시작한다. d로 방향을 설정하여 해당 방향으로 한 칸 옮겨 초기화 한다.
# 뱀의 머리에 해당하는 부분이 배열을 벗어나거나 자기 몸에 부딪치면 return 한다.
# 이 때 return 값은 뱀 대가리가 한 칸 전에 위치한 곳의 값에서 +1한 값이다.
# 뱀이 진행하며 배열의 값을 이전 위치의 값에서 +1한 값으로 설정하여 뱀의 이동 길이를 나타낸다.
# 뱀의 방향 변환하는 리스트가 비어있지 않다면 방향 전활을 해야할 경우를 고려한다.
# 배열의 값과 방향 전환 타이밍의 값이 같다면 방향 전환을 한다. d의 값을 증가 혹은 감소 (0 ~ 3)
# 뱀이 한 칸 이동하면 snake 리스트에 이동한 칸의 좌표를 append한다. 이동한 좌표에 사과가 있다면 그대로 유지하고
# 사과가 없는 빈 칸이면 snake리스트에서 제일 왼쪽 위치를 pop한다. 이런 방식으로 뱀의 길이를 조절한다. 따라서 이동할 때마다
# 뱀의 위치가 실시간으로 반영된다.

import sys
sys.setrecursionlimit(10000)

n = int(input())
k = int(input())

apple = [list(map(int, input().split())) for _ in range(k)]
for i in apple:
    i[0] -= 1
    i[1] -= 1
print(apple)
l = int(input())

direct = [list(input().split()) for _ in range(l)]

#print(apple, direct)

room = [[0] * n for _ in range(n)]

snake = [(0, 0)]

# right down left up
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def search(x, y, d):

    nx = x + dx[d]
    ny = y + dy[d]
    #print(room)
    #print([nx, ny], snake)
    if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
        #print(room)
        return room[x][y] + 1
    else:
        room[nx][ny] = room[x][y] + 1
        if direct:
            if int(direct[0][0]) == room[nx][ny]:
                if direct[0][1] == 'D':
                    d = (d + 1) % 4
                elif direct[0][1] == 'L':
                    d = d - 1 if d - 1 != -1 else 3
                direct.pop(0)
        snake.append((nx, ny))
        if [nx, ny] in apple:
            apple.remove([nx, ny])
            #print(snake)
        else:
            snake.pop(0)
            #print(snake)

        return search(nx, ny, d)

print(search(0, 0, 0))


