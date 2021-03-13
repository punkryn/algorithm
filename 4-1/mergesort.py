def mergesort(arr, p, q):
    if p < q:
        k = (p + q) // 2
        mergesort(arr, p, k)
        mergesort(arr, k + 1, q)
        merge(arr, p, k, q)

def merge(arr, p, k, q):
    c = []
    i = p
    j = k + 1

    while i <= k and j <= q:
        if arr[i] < arr[j]:
            c.append(arr[i])
            i += 1
        elif arr[i] > arr[j]:
            c.append(arr[j])
            j += 1
        else:
            c.append(arr[i])
            c.append(arr[j])
            i += 1
            j += 1

    while i <= k:
        c.append(arr[i])
        i += 1

    while j <= q:
        c.append(arr[j])
        j += 1

    j = 0
    print(c, arr)
    for i in range(p, q + 1):
        arr[i] = c[j]
        j += 1

arr = [6, 1, 3, 9, 4, 5, 8, 2, 7]
mergesort(arr, 0, 8)
print(arr)