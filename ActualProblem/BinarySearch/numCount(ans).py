# 7 2
# 1 1 2 2 2 2 3

def count(matrix, n, x):

    l = left(matrix, x, 0, n - 1)

    if l == None:
        return 0
    r = right(matrix, x, 0, n - 1, n)
    count = r - l + 1

    return count


def left(matrix, x, start, end):
    mid = (start + end) // 2

    if start > end:
        return None

    if (mid == 0 or matrix[mid - 1] < x) and matrix[mid] == x:
        return mid
    elif matrix[mid] >= x:
        return left(matrix, x, start, mid - 1)
    else:
        return left(matrix, x, mid + 1, end)

def right(matrix, x, start, end, n):
    mid = (start + end) // 2

    if start > end:
        return None

    if ((mid == n - 1 or matrix[mid + 1] > x) and matrix[mid] == x):
        return mid
    elif matrix[mid] > x:
        return right(matrix, x, start, mid - 1, n)
    else:
        return right(matrix, x, mid + 1, end, n)

n, x = map(int, input().split())

matrix = list(map(int, input().split()))

print(count(matrix, n, x))