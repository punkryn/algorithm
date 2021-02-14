n, m = map(int, input().split())

height = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid
    return None

intList = [i for i in range(max(height) + 1)]
#print(intList)

target = 0
result = 0
start = 0
end = len(intList) - 1
mid = 0
total = 0
while start <= end:
    result = 0
    mid = (start + end) // 2
    target = mid
    for item in height:
        if item > target:
            result += (item - target)

    #print(result, m)
    if result >= m:
        total = mid
        start = mid + 1
    elif result < m:
        end = mid - 1
    else:
        pass

print(mid, result, total)