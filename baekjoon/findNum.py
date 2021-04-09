# https://acmicpc.net/problem/1920

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

def binarySearch(m, left, right):
    mid = (left + right) // 2

    if left <= right:
        if m < an[mid]:
            return binarySearch(m, left, mid - 1)
        elif m > an[mid]:
            return binarySearch(m, mid + 1, right)
        else:
            return mid
    else:
        return -1

n = int(input())
an = list(map(int, input().split()))
an.sort()

m = int(input())
mlist = list(map(int, input().split()))

for m in mlist:
    if (binarySearch(m, 0, len(an) - 1)) != -1:
        print(1)
    else:
        print(0)