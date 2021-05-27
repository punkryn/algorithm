import random
import heapq

def check(arr, n):
    current = -1
    for i in range(n):
        if arr[i] >= current:
            current = arr[i]
        else:
            return False
    return True

def bubble(arr, n):
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def selection(arr):
    for i in range(len(arr) - 1):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[minimum] > arr[j]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]

    return arr

def insertionSort(arr, n):
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1

        arr[j + 1] = current
    return arr

def shell(arr, n, gap):
    for h in gap:
        for i in range(h, len(arr)):
            current = arr[i]
            j = i
            while j >= h and arr[j - h] > current:
                arr[j] = arr[j - h]
                j = j - h

            arr[j] = current

    return arr

def heapSort(arr, n):
    heapq._heapify_max(arr)
    arr.insert(0, -1)
    heapSize = n
    for i in range(n):
        arr[1], arr[heapSize] = arr[heapSize], arr[1]
        heapSize -= 1
        downHeap(arr, heapSize)

    arr.pop(0)
    return arr


def downHeap(arr, heapSize):
    i = 1
    while True:
        vmax = 0
        lflag = False
        rflag = False
        if (i * 2) <= heapSize and arr[i * 2] > arr[i] and vmax < arr[i * 2]:
            vmax = arr[i * 2]
            lflag = True

        if (i * 2 + 1) <= heapSize and arr[i * 2 + 1] > arr[i] and vmax < arr[i * 2 + 1]:
            rflag = True

        if not lflag and not rflag:
            break
        elif rflag:
            arr[i], arr[i * 2 + 1] = arr[i * 2 + 1], arr[i]
            i = i * 2 + 1
        elif lflag:
            arr[i], arr[i * 2] = arr[i * 2], arr[i]
            i = i * 2


def getrdx(l, modulus):
    maxi = 0
    for val in l:
        digit = 0
        while val > 0:
            digit += 1
            val //= modulus
        if digit > maxi:
            maxi = digit
    return maxi

def radix_sort(l):
    radix, modulus, div = 10, 10, 1
    nordx = getrdx(l, modulus)
    for i in range(nordx):
        buckets = [[] for i in range(radix)]
        for value in l:
            buckets[(value % modulus) // div].append(value)

        modulus, div = modulus * 10, div * 10
        l = []
        for x in buckets:
            l.extend(x)
    return l

arr = []
random.seed(123)
n = 2000
for _ in range(n):
    arr.append(random.randint(0, 100000))

print("Bubble")
bList = bubble(arr.copy(), n)
print(bList)
if check(bList, n):
    print("Sorted")
else:
    print("not Sorted")

print("\nSelection")
sList = selection(arr.copy())
print(sList)
if check(sList, n):
    print("Sorted")
else:
    print("not Sorted")


print("\nInsertion")
iList = insertionSort(arr.copy(), n)
print(iList)
if check(iList, n):
    print("Sorted")
else:
    print("not Sorted")


print("\nShell")
gap = [4, 1]
shellList = shell(arr.copy(), n, gap)
print(shellList)
if check(shellList, n):
    print("Sorted")
else:
    print("not Sorted")


print("\nHeap")
hList = heapSort(arr.copy(), n)
print(hList)
if check(hList, n):
    print("Sorted")
else:
    print("not Sorted")

print("\nRadix")
rList = radix_sort(arr.copy())
print(rList)
if check(rList, n):
    print("Sorted")
else:
    print("not Sorted")
