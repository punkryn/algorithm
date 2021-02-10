def solution(key, lock):
    answer = False

    length = len(key)

    key_place = []
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                key_place.append([i, j])

    hole_place = []
    for i in range(length):
        for j in range(length):
            if lock[i][j] == 0:
                hole_place.append([i, j])

    hole_num = len(hole_place)

    print(key_place, hole_place, hole_num)
    for _ in range(4):
        print(key_place)
        for hole in hole_place:
            count = 0
            for key in key_place:
                row_diff = (hole[0] - key[0])
                col_diff = (hole[1] - key[1])
                count = 0
                hit_block = False
                #print('hole, key, row_diff, col_diff')
                #print(hole, key, row_diff, col_diff)
                for key2 in key_place:
                    for hole2 in hole_place:
                        if 0 <= key2[0] + row_diff < length and 0 <= key2[1] + col_diff < length:
                            if lock[key2[0] + row_diff][key2[1] + col_diff] == 1:
                                #print('hit')
                                hit_block = True

                            if key2[0] + row_diff == hole2[0] and key2[1] + col_diff == hole2[1]:
                                count += 1

                if count == hole_num and not hit_block:

                    return True

        key_place = rotate(key_place, length)

    return answer

def rotate(key_place, n):
    # rotate_key = [[0] * len(key) for _ in range(len(key))]

    #n = len(key)

    # for i in range(len(key)):
    #     for j in range(len(key)):
    #         rotate_key[j][n - 1 - i] = key[i][j]

    tmp = []
    for key in key_place:
        i = key[0]
        j = key[1]
        tmp.append([j, n - 1 - i])

    # for x in range(n):
    #     for y in range(n):
    #         print(rotate_key[x][y], end=' ')
    #     print()

    return tmp

# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[0, 0, 1], [1, 1, 1], [1, 1, 1]]

# 4
# 1 1 0 0
# 0 1 1 0
# 0 0 0 0
# 0 0 0 0
# 1 1 1 1
# 1 1 0 0
# 1 1 1 0
# 1 1 1 1


l = int(input())
key = []
for _ in range(l):
    key.append(list(map(int, input().split())))

lock = []
for _ in range(l):
    lock.append(list(map(int, input().split())))

print(key, lock)
if (solution(key, lock)):
    print('true')
else:
    print('false')