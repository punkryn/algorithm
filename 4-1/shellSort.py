def shell(arr, gap):
    for h in gap:
        for i in range(h, len(arr)):
            current = arr[i]
            j = i
            while j >= h and arr[j - h] > current:
                arr[j] = arr[j - h]
                j = j - h

            arr[j] = current

    print(arr)

arr = [5, 8, 1, 2, 0, 6, 9, 3, 7, 4]
gap = [4, 1]

shell(arr, gap)

