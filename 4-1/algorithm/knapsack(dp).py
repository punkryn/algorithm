def knapsack(n, C):
    for i in range(1, n + 1):
        for w in range(1, C + 1):
            #print(i, w)
            if item[i-1][0] > w:
                K[i][w] = K[i - 1][w]
            else:
                K[i][w] = max(K[i - 1][w], K[i-1][w - item[i-1][0]] + item[i-1][1])

            for x in range(n + 1):
                for y in range(C + 1):
                    print(K[x][y], end=' ')
                print()
            print()



item = [[5, 10], [4, 40], [6, 30], [3, 50]]
n = 4
C = 10
K = []

for x in range(n + 1):
    K.append([])
    for y in range(C + 1):
        K[x].append(0)



knapsack(n, C)

for i in range(n + 1):
    for j in range(C + 1):
        print(K[i][j], end=' ')
    print()