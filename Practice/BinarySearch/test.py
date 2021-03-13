import time

def binary_search(arr, target, start, end):
    mid = (start + end) // 2

    if start > end:
        return None

    if arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return mid

def binary_search_rep(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid
    return None

array = [i for i in range(10000000)]

start = time.time()
print(binary_search(array, 3, 0, len(array)-1))
#end = time.time()
print((time.time() - start))
print(binary_search_rep(array, 3, 0, len(array)-1))
