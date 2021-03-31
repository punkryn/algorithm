# https://www.acmicpc.net/problem/1946

# 2
# 5
# 3 2
# 1 4
# 4 1
# 2 3
# 5 5
# 7
# 3 6
# 7 3
# 4 2
# 1 4
# 5 7
# 2 5
# 6 1

from sys import stdin

for _ in range(int(input())):
    n = int(stdin.readline())
    score = [list(map(int, stdin.readline().split())) for _ in range(n)]

    score.sort(key=lambda x: x[0])
    #print(score)
    # s2 = (sorted(score, key=lambda x: x[1]))

    minimum = score[0][1]
    result = n

    for i in range(1, len(score)):
        if score[i][1] > minimum:
            #print('i', i)
            result -= 1
        elif score[i][1] < minimum:
            minimum = score[i][1]

    print(result)

