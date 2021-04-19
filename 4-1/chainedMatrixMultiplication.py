matrix = [(10, 20), (20, 5), (5, 15), (15, 30)]

n = len(matrix)

C = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

order = [[-1] * (n + 1) for _ in range(n + 1)]

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
                order[i][j] = (i, k, j)

# print(last_index_i, last_k, last_index_j, last_c)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(order[i][j], end=' ')
    print()
print()

# print("행렬 곱의 순서:", "C[" + str(last_index_i) + ', ' + str(last_k) + ']',
#               "C[" + str(last_k + 1) + ', ' + str(last_index_j) + ']')

# 1 3 4
def multiplicationOrder(i, k, j):
    if k - i <= 1 and j - k - 1 <= 1:
        print("C[" + str(i) + ', ' + str(k) + ']', 'C[' + str(k + 1) + ', ' + str(j) + ']')
        return
    elif k - i > 1:
        print("C[" + str(i) + ', ' + str(k) + ']', 'C[' + str(k + 1) + ', ' + str(j) + ']')
        i, k, j = order[i][k]
        multiplicationOrder(i, k, j)
    elif j - k - 1 > 1:
        print("C[" + str(i) + ', ' + str(k) + ']', 'C[' + str(k + 1) + ', ' + str(j) + ']')
        i, k, j = order[k+1][j]
        multiplicationOrder(i, k, j)

#multiplicationOrder(last_index_i, last_k, last_index_j)
multiplicationOrder(1, 3, 4)

