import sys
sys.setrecursionlimit(5000)

def solution(board):
    answer = 0

    length = len(board)
    global min_value
    visited = [[0] * length for _ in range(length)]
    rotate_visited = [[False] * length for _ in range(length)]
    dfs(((0, 0), (0, 1)), visited, length, board, 1, rotate_visited)

    answer = visited[length-1][length-1]

    answer = min_value

    return answer - 1

def dfs(start, visited, length, board, counter, rotate_visited):
    p1, p2 = start

    x1, y1 = p1
    x2, y2 = p2

    global min_value

    visited[x1][y1] = counter
    visited[x2][y2] = counter

    if (x1, y1) == (length - 1, length - 1) or (x2, y2) == (length - 1, length - 1):
        #print('11111111111111111111111111111111111111111111111')
        #visited[length-1][length-1] = min(visited[x1][y1], counter)
        if min_value > counter:
            min_value = counter
        return



    # for i in range(length):
    #     for j in range(length):
    #         print(visited[i][j], end=' ')
    #     print()
    # print()

    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]

        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]

        if not (0 <= nx1 < length and 0 <= ny1 < length):
            continue
        if not (0 <= nx2 < length and 0 <= ny2 < length):
            continue

        if visited[nx1][ny1] and visited[nx2][ny2]:
            continue

        if board[nx1][ny1] == 1 or board[nx2][ny2] == 1:
            continue

        #print(nx1, ny1, nx2, ny2)

        pre1 = visited[nx1][ny1]
        pre2 = visited[nx2][ny2]

        dfs(((nx1, ny1), (nx2, ny2)), visited, length, board, counter + 1, rotate_visited)

        visited[nx1][ny1] = pre1
        visited[nx2][ny2] = pre2

    for i in range(4, 6):
        index = i - 4

        axis = (x1, y1)
        pos = (x2, y2)

        # if index == 0:
        #     ob = (x2 + y2 - 1, abs(x2 - y2 - 1))
        # elif index == 1:
        #     ob = (abs(y2 - x2 - 1), y2 + x2 - 1)

        nx, ny, ob = rotate(axis, pos, index)

        if not (0 <= nx < length and 0 <= ny < length):
            continue

        if not (0 <= ob[0] < length and 0 <= ob[1] < length):
            continue


        if visited[nx][ny]:
            continue

        if board[ob[0]][ob[1]] == 1:
            continue

        if visited[nx][ny] + 1 == visited[pos[0]][pos[1]]:
            continue

        if board[nx][ny] == 1:
            continue

        pre = visited[nx][ny]

        #print('1', axis, pos, nx, ny, ob, index)
        dfs((axis, (nx, ny)), visited, length, board, counter + 1, rotate_visited)

        visited[nx][ny] = pre

        ########################################################

    for i in range(4, 6):
        index = i - 4
        axis = (x2, y2)
        pos = (x1, y1)

        # if index == 0:
        #     ob = (x1 + y1 - 1, abs(x1 - y1 - 1))
        # elif index == 1:
        #     ob = (abs(y1 - x1 - 1), x1 + y1 - 1)

        nx, ny, ob = rotate(axis, pos, index)
        if not (0 <= nx < length and 0 <= ny < length):
            continue

        if not (0 <= ob[0] < length and 0 <= ob[1] < length):
            continue


        if visited[nx][ny]:
            continue

        if board[ob[0]][ob[1]] == 1:
            continue

        if visited[nx][ny] + 1 == visited[pos[0]][pos[1]]:
            continue

        if board[nx][ny] == 1:
            continue

        pre = visited[nx][ny]

        #print('2', nx, ny, ob)
        dfs((axis, (nx, ny)), visited, length, board, counter + 1, rotate_visited)

        visited[nx][ny] = pre

def rotate(axis, pos, d):
    x, y = pos
    x_, y_ = axis
    clockwise = 0
    counterclockwise = 1

    if x == x_ and y > y_:
        if d == clockwise:
            return x_ + 1, y_, (x + 1, y)
        else:
            return x_ - 1, y_, (x - 1, y)
    elif x == x_ and y < y_:
        if d == clockwise:
            return x_ - 1, y_, (x - 1, y)
        else:
            return x_ + 1, y_, (x + 1, y)
    elif x < x_ and y == y_:
        if d == clockwise:
            return x_, y_ + 1, (x, y + 1)
        else:
            return x_, y_ - 1, (x, y - 1)
    else:
        if d == clockwise:
            return x_, y_ - 1, (x, y - 1)
        else:
            return x_, y_ + 1, (x, y + 1)


# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

clock = [0, 1]

min_value = 1e9

#board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
board = [[0,0,0,0,1],[1,1,0,0,1],[1,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]
print(solution(board))
