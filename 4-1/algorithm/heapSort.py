import heapq
def heapSort(arr, n):
    heapq._heapify_max(arr)
    arr.insert(0, -1)
    heapSize = n
    for i in range(n):
        print(arr)
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

arr = [90, 60, 80, 50, 30, 70, 10, 20, 40]
heapSort(arr, 9)
print(arr)