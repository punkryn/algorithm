# 재귀

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return mid

#arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(arr, 4, 0, len(arr) - 1))

# 반복문

def binary_search_rep(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return mid
    return None

print(binary_search_rep(arr, 3, 0, len(arr) - 1))