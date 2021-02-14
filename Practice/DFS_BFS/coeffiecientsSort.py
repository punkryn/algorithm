arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

mat = [0] * (max(arr) + 1)

for i in arr:
    mat[i] += 1
print(mat)

for j in range(len(mat)):
    for k in range(mat[j]):
        print(j, end=' ')
