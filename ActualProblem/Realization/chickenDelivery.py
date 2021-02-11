from itertools import combinations

#n, m = map(int, input().split())

#mat = [list(map(int, input().split())) for _ in range(n)]

#print(mat)

testcase = ['5 3\n0 0 1 0 0\n0 0 2 0 1\n0 1 2 0 0\n0 0 1 0 0\n0 0 0 0 2',
            '5 2\n0 2 0 1 0\n1 0 1 0 0\n0 0 0 0 0\n2 0 0 1 1\n2 2 0 1 2',
            '5 1\n1 2 0 0 0\n1 2 0 0 0\n1 2 0 0 0\n1 2 0 0 0\n1 2 0 0 0',
            '5 1\n1 2 0 2 1\n1 2 0 2 1\n1 2 0 2 1\n1 2 0 2 1\n1 2 0 2 1',
            '2 1\n0 0\n2 1']

for case in testcase:
    mat = []
    tmp = case.split('\n')
    for i in range(len(tmp)):
        if i == 0:
            n, m = map(int, tmp[i].split())
            continue
        mat.append(list(map(int, tmp[i].split())))
#print(n, m)
#print(mat)

    house = []
    chicken = []

    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                house.append([i, j])

            elif mat[i][j] == 2:
                chicken.append([i, j])

    for i in range(1, m + 1):
        comb = combinations(chicken, i)

        min_comb = 10000
        min_value = 10000
        for item in comb:
            #print('item', item)
            distance = [10000 for _ in range(len(house))]
            for i in item:
                x, y = i
                for j, ho in enumerate(house):
                    #print('ho', ho)
                    hx, hy = ho
                    result = 0
                    result += (x - hx if x - hx > 0 else hx - x)
                    result += (y - hy if y - hy > 0 else hy - y)
                    if distance[j] > result:
                        distance[j] = result
                    # distance[j].append(result)
            #print(distance, end='\n\n')
            final = 0
            # for k in range(len(item)):
            #     for l in range(len(distance)):
            #         final += distance[l][k]

            for k in distance:
                final += k

            if min_value > final:
                min_value = final

        if min_comb > min_value:
            min_comb = min_value
        # print('1', min_value)
    print('2', min_comb)


from itertools import combinations

n, m = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]

#print(mat)

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            house.append([i, j])

        elif mat[i][j] == 2:
            chicken.append([i, j])

min_comb = 10000
for co in range(1, m + 1):
    comb = combinations(chicken, co)

    min_value = 10000
    for item in comb:
        #print('item', item)
        distance = [10000 for _ in range(len(house))]
        for i in item:
            x, y = i
            for j, ho in enumerate(house):
                #print('ho', ho)
                hx, hy = ho
                result = 0
                result += (x - hx if x - hx > 0 else hx - x)
                result += (y - hy if y - hy > 0 else hy - y)
                if distance[j] > result:
                    distance[j] = result
                # distance[j].append(result)
        #print(distance)
        final = 0
        # for k in range(len(item)):
        #     for l in range(len(distance)):
        #         final += distance[l][k]

        for k in distance:
            final += k

        if min_value > final:
            min_value = final

    #print(min_value)
    if min_comb > min_value:
        min_comb = min_value
print(min_comb)