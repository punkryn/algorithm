# 7 2
# 1 1 2 2 2 2 3

# 7 4
# 1 1 2 2 2 2 3

# 7 3
# 1 1 2 2 3 3 4

n, x = map(int, input().split())

matrix = list(map(int, input().split()))

#print(matrix)

tmp = []

def bs(x, start, end):
    mid = (start + end) // 2
    #print('start, end', start, end)
    if start < end:
        if matrix[mid] < x:
            bs(x, mid + 1, end)
        elif matrix[mid] > x:
            bs(x, start, mid - 1)
        else:
            tmp.append(mid)
            bs(x, mid + 1, end)
            bs(x, start, mid - 1)
    else:
        if matrix[mid] == x:
            tmp.append(mid)

(bs(x, 0, n - 1))
print(tmp)
if tmp:
    print(max(tmp) - min(tmp) + 1)
else:
    print(-1)