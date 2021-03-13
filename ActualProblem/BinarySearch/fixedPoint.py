# 5
# -15 -6 1 3 7

# 7
# -15 -4 2 8 9 13 15

# 7
# -15 -4 3 8 9 13 15

def bs(matrix, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    print(start, end, mid)
    if matrix[mid] == mid:
        tmp.append(mid)
    elif matrix[mid] > mid:
        bs(matrix, mid + 1, end)
        bs(matrix, start, mid - 1)
    else:
        bs(matrix, mid + 1, end)
        bs(matrix, start, mid - 1)

n = int(input())

matrix = list(map(int, input().split()))

tmp = []

bs(matrix, 0, n - 1)

if tmp:
    print(tmp.pop())
else:
    print(-1)