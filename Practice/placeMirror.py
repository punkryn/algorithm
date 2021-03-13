# https://www.acmicpc.net/problem/2151   2151
# 5
# ***#*
# *.!.*
# *!.!*
# *.!.*
# *#***

# 5
# *****
# *!.!*
# #.!!#
# *.!!*
# *****

# 5
# *****
# *.!.#
# #.!!*
# *.!!*
# *****

# 5
# **#**
# *...*
# *!!!*
# *.!.*
# *#***

from sys import stdin
U = 0
D = 1
L = 2
R = 3

n = int(input())

room = [stdin.readline().strip() for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def direction(room, pos):
    # 상 하 좌 우
    #d = [0, 1, 2, 3]
    d = {}
    #print(room[pos[0] - 1][pos[1]], room[pos[0] + 1][pos[1]], room[pos[0]][pos[1] - 1], room[pos[0]][pos[1] + 1])

    if  pos[0] - 1 >= 0 and room[pos[0] - 1][pos[1]] != '*':
        #d.remove(0)
        d[0] = (pos[0] - 1, pos[1])

    if pos[0] + 1 < n and room[pos[0] + 1][pos[1]] != '*':
        d[1] = (pos[0] + 1, pos[1])

    if pos[1] - 1 >= 0 and room[pos[0]][pos[1] - 1] != '*':
        d[2] = (pos[0], pos[1] - 1)

    if pos[1] + 1 < n and room[pos[0]][pos[1] + 1] != '*':
        d[3] = (pos[0], pos[1] + 1)

    return d

def mirror(room, light, d, lightQueue):

    if d == U or d == D:
        if room[light[0]][light[1] - 1] != '*' and visited[light[0]][light[1] - 1] == 0:
            lightQueue.append(2)
        if room[light[0]][light[1] + 1] != '*' and visited[light[0]][light[1] + 1] == 0:
            lightQueue.append(3)
    if d == L or d == R:
        if room[light[0] - 1][light[1]] != '*' and visited[light[0] - 1][light[1]] == 0:
            lightQueue.append(0)
        if room[light[0] + 1][light[1]] != '*' and visited[light[0] + 1][light[1]] == 0:
            lightQueue.append(1)

door_pos = []
light = ()
for i in range(n):
    for j in range(n):
        if room[i][j] == '#':
            door_pos.append((i, j))
            light = door_pos[0]
        if room[i][j] == '*':
            visited[i][j] = 1

visited[light[0]][light[1]] = 1

#print(light)
lightQueue = []
for d in direction(room, light).values():
    lightQueue.append(d)

print(lightQueue)

lightStack = []
lightCountStack = [0]
count = 0
breakCount = False
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
preMirrorPos = []
pmp = ()
while lightQueue:
    print('lightQueue', lightQueue)
    print('lightStack', lightStack)
    d = lightQueue.pop()
    for i in range(n):
        for j in range(n):
            print(visited[i][j], end='')
        print()

    while room[d[0]][d[1]] != '!':
        light = d
        visited[light[0]][light[1]] = 1
        print(light)
        if room[light[0]][light[1]] == '*':
            if lightStack:
                light = lightStack.pop()

            breakCount = True
            break

        if door_pos[1] == light:
            breakCount = True
            lightQueue.clear()
            break

    # while room[light[0] + dx[d]][light[1] + dy[d]] != '!':
    #     light = (light[0] + dx[d], light[1] + dy[d])
    #     visited[light[0]][light[1]] = 1
    #     print(light)
    #     if room[light[0]][light[1]] == '*':
    #         if lightStack:
    #             light = lightStack.pop()
    #             #preMirrorPos.pop()
    #
    #         breakCount = True
    #         break
    #
    #     #print(door_pos[1], (light[0], light[1]))
    #     if door_pos[1] == (light[0], light[1]):
    #         breakCount = True
    #         lightQueue.clear()
    #         break

    if breakCount:
        breakCount = False
        continue

    light = (light[0] + dx[d], light[1] + dy[d])
    print(light)
    preMirrorPos.append(light)

    if room[light[0]][light[1]] == '!':
        count += 1
        #print('lightstack', lightStack, light)
        if count == 1:
            visited[light[0]][light[1]] = 1

        elif count > 1:
            if lightStack:
                pmp = lightStack[-1]
            #print('pmp', pmp)

            visited[light[0]][light[1]] = (visited[pmp[0]][pmp[1]] + 1)


        lightStack.append(light)
        mirror(room, light, d, lightQueue)
        continue


print(visited[preMirrorPos[-1][0]][preMirrorPos[-1][1]])