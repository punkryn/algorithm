# 답을 보기 전
# 2차원 배열에서 어떤 특정한 위치의 값이 이미 정해져 있으면 그 뒤의 값은 항상 같다.
# 즉 어떠한 위치에서의 경로는 항상 일정하다. 따라서 2차원 배열에서 특정 위치의 값이 정해져 있으면
# 그 뒤는 더 이상 경로를 찾지 않고 정해진 값을 사용한다.
# 정해진 값이 없이 마지막 열까지 탐색을 완료하면 스택에 쌓여있던 열의 위치와 해당 위치의 값을
# 이용하여 열을 거슬러 올라가며 해당 위치의 값을 결정한다.

# 답
# 똑같이 2차원 테이블로 구성하였다. 다른 점은 1열은 초기화하고 2열부터 진행하여
# 왼쪽위, 왼쪽, 왼쪽 아래 세 가지의 경우 중 가장 큰 값이 되는 값을 해당 위치에 넣어
# 최종적인 값은 가장 마지막열에 넣는다.

# 3
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
# 3 3
# 1 3 3 2 1 4 0 6 4

from sys import stdin

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))

    mine = [[-1] * (m + 1) for _ in range(n + 2)]

    count = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            mine[i][j] = tmp[count]
            count += 1
    #print(mine)

    maxindex = [[-1] * (m + 1) for _ in range(n + 1)]

    max_value = 0
    for i in range(1, n + 1):
        total = 0
        stack = []
        row = i
        for j in range(1, m + 1):
            #print('row', row)
            #print(stack)
            if j == 1:
                stack.append((i, total))
                total += mine[i][j]
                # maxindex[i][j] = mine[i][j]
            else:

                max_of_3 = max(mine[row - 1][j], mine[row][j], mine[row + 1][j])

                if max_of_3 == mine[row - 1][j]:
                    row = row - 1
                elif max_of_3 == mine[row + 1][j]:
                    row = row + 1
                else:
                    row = row
                #print('row, j', row, j, i)

                if maxindex[row][j] != -1:
                    tmp = maxindex[row][j]
                    for k in range(j - 1, 0, -1):
                        r, value = stack.pop()

                        tmp += (mine[r][k])
                        maxindex[r][k] = tmp

                    # for a in range(1, n + 1):
                    #     for b in range(1, m + 1):
                    #         print(maxindex[a][b], end=' ')
                    #     print()
                    # print()

                    max_value = max(max_value, maxindex[i][1])

                    break

                stack.append((row, total))
                total += mine[row][j]

                if j == m:
                    for k in range(j, 0, -1):
                        row, value = stack.pop()
                        maxindex[row][k] = total - value

                # for a in range(1, n + 1):
                #     for b in range(1, m + 1):
                #         print(maxindex[a][b], end=' ')
                #     print()
                # print()

                max_value = max(max_value, maxindex[i][1])

    # for x in range(1, n + 1):
    #     if max_value < maxindex[x][1]:
    #         max_value = maxindex[x][1]

    for a in range(1, n + 1):
        for b in range(1, m + 1):
            print(maxindex[a][b], end=' ')
        print()
    print()
    print(max_value)