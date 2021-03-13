from bisect import bisect_left, bisect_right

def bs(matrix, left_value, right_value):
    right_index = bisect_right(matrix, right_value)
    left_index = bisect_left(matrix, left_value)

    return right_index - left_index

n, x = map(int, input().split())

matrix = list(map(int, input().split()))

count = bs(matrix, x, x)

if count == 0:
    print(-1)
else:
    print(count)