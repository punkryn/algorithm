d = [
    [0, 4, 2, 5, 100],
    [100, 0, 1, 100, 4],
    [1, 3, 0, 1, 2],
    [-2, 100, 100, 0, 2],
    [100, -3, 3, 1, 0]
]

n = 5

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][k] + d[k][j], d[i][j])

    for x in range(n):
        for y in range(n):
            print(d[x][y], end=' ')
        print()
    print()