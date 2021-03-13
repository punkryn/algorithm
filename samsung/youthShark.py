# 7 6 2 3 15 6 9 8
# 3 1 1 8 14 7 10 1
# 6 1 13 6 4 3 11 4
# 16 1 8 7 5 2 12 2

# https://www.acmicpc.net/problem/19236

import copy

def movefish(space, shark_pos):
    #rotate = [0] * 17
    for fish in range(1, 17):
        endSw = False
        for i in range(4):
            for j in range(4):
                if space[i][j][0] == fish:

                    for aaa in range(8):
                        #ni = i + dx[space[i][j][1]]
                        #nj = j + dy[space[i][j][1]]
                        ni = i + dx[aaa]
                        nj = j + dy[aaa]


                        if 0 <= ni < 4 and 0 <= nj < 4 and not (ni == shark_pos[0] and nj == shark_pos[1]):
                            space[ni][nj], space[i][j] = space[i][j], space[ni][nj]
                            endSw = True

                    # else:
                    #     for k in range(1, 9):
                    #         di = (space[i][j][1] + k) % 8
                    #         ni = i + dx[di]
                    #         nj = j + dy[di]
                    #
                    #         if 0 <= ni < 4 and 0 <= nj < 4 and di > 0 and not (ni == shark_pos[0] and nj == shark_pos[1]):
                    #             # print('ni, nj, di', ni, nj, di, i, j, fish)
                    #             space[i][j][1] = di
                    #             space[ni][nj], space[i][j] = space[i][j], space[ni][nj]
                    #
                    #             endSw = True
                    #
                    #             #rotate[fish] = k
                    #             # print('fish, k', fish, k)
                    #             break
                    # break

            if endSw:
                break

    #return rotate
        # for a in range(4):
        #     for b in range(4):
        #         print(space[a][b], end=' ')
        #     print()
        # print()

# def reverse(space, rotate):
#     # print(rotate)
#     for fish in range(16, 0, -1):
#         endSw = False
#         for i in range(4):
#             for j in range(4):
#                 if space[i][j][0] == fish:
#                     ni = i + dxr[space[i][j][1]]
#                     nj = j + dyr[space[i][j][1]]
#
#                     if 0 <= ni < 4 and 0 <= nj < 4 and space[ni][nj][0] != shark:
#                         if rotate[fish] > 0:
#                             di = (space[i][j][1] - rotate[fish]) if space[i][j][1] - rotate[fish] > 0 else 8 + (
#                                         space[i][j][1] - rotate[fish])
#                             space[i][j][1] = di
#
#                         space[ni][nj], space[i][j] = space[i][j], space[ni][nj]
#
#                         endSw = True
#
#                     # else:
#                     #     for k in range(7, 0, -1):
#                     #         di = (space[i][j][1] + k) % 8
#                     #         ni = i + dxr[di]
#                     #         nj = j + dyr[di]
#                     #
#                     #         if 0 <= ni < 4 and 0 <= nj < 4 and space[ni][nj][0] != shark and di > 0:
#                     #             # print('ni, nj, di', ni, nj, di, i, j, fish)
#                     #
#                     #             space[ni][nj], space[i][j] = space[i][j], space[ni][nj]
#                     #
#                     #             endSw = True
#                     #             break
#                     break
#
#             if endSw:
#                 break

# def process(space, value_count, stack, shark_pos):
#     global max_value
#     if not stack:
#         return
#
#     while stack:
#         print('stack', stack)
#         print('max', max_value, value_count)
#         x, y = stack.pop()
#         value = space[x][y][0]
#
#         rev = [[0] * 4 for _ in range(4)]
#         for xx in range(4):
#             for yy in range(4):
#                 rev[xx][yy] = space[xx][yy]
#
#         ori = space[x][y]
#         print('ori', ori)
#
#         ori2 = space[shark_pos[0]][shark_pos[1]]
#         print('ori2', ori2)
#
#         space[shark_pos[0]][shark_pos[1]] = [0, 0]
#         space[x][y] = [shark, space[x][y][1]]
#
#         value_count += value
#         print('value_count', value_count)
#         for ix in range(4):
#             for jx in range(4):
#                 print(space[ix][jx], end=' ')
#             print()
#         print()
#
#         # ori = []
#         # for tmpx in range(4):
#         #     ori.append([])
#         #     for tmpy in range(4):
#         #         ori[tmpx].append(space[tmpx][tmpy][1])
#
#         #print(1, ori, id(ori))
#
#         rotate = movefish(space)
#
#         cur_stack_size = len(stack)
#         for leverage in range(1, 4):
#             nx = x + dx[space[x][y][1]] * leverage
#             ny = y + dy[space[x][y][1]] * leverage
#
#             if 0 <= nx < 4 and 0 <= ny < 4 and space[nx][ny][0] != 0:
#                 stack.append((nx, ny))
#
#
#         if cur_stack_size == len(stack):
#             if max_value < value_count:
#                 max_value = value_count
#
#             value_count -= value
#
#             # reverse(space, rotate)
#             for xx in range(4):
#                 for yy in range(4):
#                     space[xx][yy] = rev[xx][yy]
#
#             print('x, y, s0, s1', x, y, shark_pos)
#
#             space[x][y] = ori
#
#             space[shark_pos[0]][shark_pos[1]] = ori2
#
#             # process(space, value_count, stack, shark_pos)
#
#             continue
#             #return
#
#         shark_pos = (x, y)
#         process(space, value_count, stack, shark_pos)
#
#         #print(2, ori, id(ori))
#
#         value_count -= value
#
#         # reverse(space, rotate)
#         for xx in range(4):
#             for yy in range(4):
#                 space[xx][yy] = rev[xx][yy]
#
#         space[x][y] = ori
#         space[shark_pos[0]][shark_pos[1]] = ori2
#
#         # process(space, value_count, stack, shark_pos)

def process(space, value_count, shark_pos):
    global max_value
    space = copy.deepcopy(space)

    x, y = shark_pos

    value_count += space[x][y][0]

    space[x][y][0] = -1

    for ix in range(4):
        for jx in range(4):
            print(space[ix][jx], end=' ')
        print()
    print()

    #print(space)

    #print(space[x][y][1])

    movefish(space, shark_pos)

    #space[x][y] = [0, space[x][y][1]]

    #print(space)
    stack = []
    for leverage in range(1, 4):
        nx = x + dx[space[x][y][1]] * leverage
        ny = y + dy[space[x][y][1]] * leverage
        # print('nx', nx, ny, x, y, space[x][y][1])
        if 0 <= nx < 4 and 0 <= ny < 4 and space[nx][ny][0] != -1:
            stack.append((nx, ny))
    print(stack)

    if len(stack) == 0:
        max_value = max(max_value, value_count)
        return

    for item in stack:
        process(space, value_count, item)


space = []
tmpcount = 0
tmplist = []
for item in [list(map(int, input().split())) for _ in range(4)]:
    tmplist2 = []
    for num in item:
        tmpcount += 1
        tmplist2.append(num)

        if tmpcount == 2:
            tmpcount = 0
            tmplist2[1] -= 1
            tmplist.append(tmplist2)
            tmplist2 = []

    space.append(tmplist)
    tmplist = []

print(space)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

shark = 17

# value_count = space[0][0][0]
max_value = 0
# space[0][0][0] = shark

# rotate = movefish(space)

for ix in range(4):
    for jx in range(4):
        print(space[ix][jx], end=' ')
    print()
print()

# reverse(space, rotate)
#
# for ix in range(4):
#     for jx in range(4):
#         print(space[ix][jx], end=' ')
#     print()
# print()

process(space, 0, (0, 0))
print(max_value)