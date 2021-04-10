# 7 2
# 1 1 2 2 2 2 3

# 8 4
# 1 1 2 2 2 2 3 3

def lower_bound(num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= num:
            right = mid - 1
        else:
            left = mid + 1
    return left

def upper_bound(num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return right

n, x = map(int, input().split())

arr = list(map(int, input().split()))

li = lower_bound(x)
ri = upper_bound(x)

if ri - li + 1 == 0:
    print(-1)
else:
    print(ri - li + 1)