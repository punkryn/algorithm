def selection(arr):
    for i in range(len(arr) - 1):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[minimum] > arr[j]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]

    print(arr)

arr = [5, 8, 1, 2, 0, 6, 9, 3, 7, 4]
selection(arr)
