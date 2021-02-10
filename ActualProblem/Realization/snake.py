# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# https://www.acmicpc.net/status?user_id=honeysleep&problem_id=3190&from_mine=1

import sys
sys.setrecursionlimit(10000)

n = int(input())
k = int(input())

apple = [list(map(int, input().split())) for _ in range(k)]
for i in apple:
    i[0] -= 1
    i[1] -= 1
#print(apple)
l = int(input())

direct = [list(input().split()) for _ in range(l)]

#print(apple, direct)

room = [[0] * n for _ in range(n)]

snake = [(0, 0)]

def search(x, y, d):
    # right down left up
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

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


