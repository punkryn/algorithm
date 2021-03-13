from sys import stdin

def binary_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, end)
    else:
        return mid

n = int(input())
nList = stdin.readline().split()
nList.sort()

m = int(input())
mList = stdin.readline().split()

for item in mList:
    result = binary_search(nList, item, 0, len(nList) - 1)
    #print(result)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')