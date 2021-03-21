# https://www.acmicpc.net/problem/14890

# 6 2
# 3 3 3 3 3 3
# 2 3 3 3 3 3
# 2 2 2 3 2 3
# 1 1 1 2 2 2
# 1 1 1 3 3 1
# 1 1 2 3 3 2

# 5 2
# 2 1 1 1 2
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1

import copy

def way(road, start, end, row):
    i = start
    sw = True
    while i < end:
        if road[row][i] == road[row][i + 1]:
            i += 1
        else:
            i += 1
            sw = False

    return sw

def way2(road, start, end, col):
    i = start
    sw = True
    while i < end:
        if road[i][col] == road[i + 1][col]:
            i += 1
        else:
            i += 1
            sw = False

    return sw

def show_slope(slope, n):
    for i in range(n):
        for j in range(n):
            print(slope[i][j], end=' ')
        print()
    print()

n, l = map(int, input().split())

road = [list(map(int, input().split())) for _ in range(n)]

slope = [[False] * n for _ in range(n)]

count = 0
for row in range(n):
    i = 0
    # print('1', way(road, 0, n - 1, row))
    if way(road, 0, n - 1, row):            # 한 줄 전체 검사
        #print(row)
        count += 1
    else:
        slope_copy = copy.deepcopy(slope)
        tmp = False
        tmp2 = False
        while i < n - 1:
            out_of_range = False
            now = road[row][i]
            visited = False

            #print('i', i, now, road[row][i + 1])

            #show_slope(slope, n)

            #print(now + 1 == road[row][i + 1], now, road[row][i + 1])

            if now == road[row][i + 1]:             # 같은 경우
                #print('!@#')
                i += 1
            elif now > road[row][i + 1] + 1 or now + 1 < road[row][i + 1]:    # 차이가 1보다 큰 경우
                slope = slope_copy
                break
            elif now == road[row][i + 1] + 1:       # 오른쪽이 낮은 경우
                #print('???')
                if i + l >= n:
                    out_of_range = True                     # 범위를 벗어남
                    slope = slope_copy
                    break

                if way(road, i + 1, i + l, row):            # 경사로 놓을 수 있음
                    for j in range(i + 1, i + l + 1):
                        if slope[row][j]:                   # 이미 놓여있음
                            visited = True
                            slope = slope_copy
                            break
                        else:
                            slope[row][j] = True

                    i += l
                else:                                       # 연속되지 않음
                    slope = slope_copy
                    break

            elif now + 1 == road[row][i + 1]:       # 왼쪽이 낮은 경우
                #print('123')
                if i - l + 1 < 0:
                    out_of_range = True
                    slope = slope_copy
                    break

                if way(road, i - l + 1, i, row):
                    for j in range(i - l + 1, i + 1):
                        if slope[row][j]:
                            #print(123)
                            visited = True
                            slope = slope_copy
                            break
                        else:
                            slope[row][j] = True

                    i += 1
                else:
                    slope = slope_copy
                    break

            if out_of_range:
                #slope = slope_copy
                tmp = True
                break

            if visited:
                tmp2 = True
                #slope = slope_copy
                break

        if i == n - 1 and not tmp and not tmp2:
            #print('2', row)
            count += 1
            #break


slope = [[False] * n for _ in range(n)]
for col in range(n):
    i = 0
    # print('1', way(road, 0, n - 1, row))
    if way2(road, 0, n - 1, col):
        #print('3', col)
        count += 1
    else:
        slope_copy = copy.deepcopy(slope)
        tmp = False
        tmp2 = False
        while i < n - 1:
            out_of_range = False
            now = road[i][col]
            visited = False

            #print('i', i, now, road[row][i + 1])

            #show_slope(slope, n)

            #print(now + 1 == road[row][i + 1], now, road[row][i + 1])

            if now == road[i + 1][col]:
                #print('!@#')
                i += 1
            elif now > road[i + 1][col] + 1 or now + 1 < road[i + 1][col]:    # 차이가 1보다 큰 경우
                slope = slope_copy
                break
            elif now == road[i + 1][col] + 1:       # 오른쪽이 낮은 경우
                #print('???')
                if i + l >= n:
                    out_of_range = True                     # 범위를 벗어남
                    slope = slope_copy
                    break

                if way2(road, i + 1, i + l, col):            # 경사로 놓을 수 있음
                    for j in range(i + 1, i + l + 1):
                        if slope[j][col]:                   # 이미 놓여있음
                            visited = True
                            slope = slope_copy
                            break
                        else:
                            slope[j][col] = True

                    i += l
                else:                                       # 연속되지 않음
                    slope = slope_copy
                    break

            elif now + 1 == road[i + 1][col]:       # 왼쪽이 낮은 경우
                #print('123')
                if i - l + 1 < 0:
                    out_of_range = True
                    slope = slope_copy
                    break

                if way2(road, i - l + 1, i, col):
                    for j in range(i - l + 1, i + 1):
                        if slope[j][col]:
                            visited = True
                            slope = slope_copy
                            break
                        else:
                            slope[j][col] = True

                    i += 1
                else:
                    slope = slope_copy
                    break

            if out_of_range:
                #slope = slope_copy
                tmp = True
                break

            if visited:
                tmp2 = True
                #slope = slope_copy
                break


        if i == n - 1 and not tmp and not tmp2:
            #print('4', col)
            count += 1
            #break

print(count)