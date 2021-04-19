matrix = [(10, 20), (20, 5), (5, 15), (15, 30)]

n = len(matrix)

C = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    C[i][i] = 0

for L in range(1, n):
    for i in range(1, n - L + 1):
        j = i + L

        for k in range(i, j):
            # print(i, j, k, matrix[i-1][0], matrix[k-1][1], matrix[j-1][1])
            tmp = C[i][k] + C[k + 1][j] + (matrix[i-1][0] * matrix[k-1][1] * matrix[j-1][1])
            if tmp < C[i][j]:
                C[i][j] = tmp

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if C[i][j] == int(1e9):
            print("INF", end=" ")
        else:
            print((C[i][j]), end=' ')
    print()