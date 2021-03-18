def mergesort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = mergesort(arr[:mid])
    high_arr = mergesort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


alist = [4, 26, 9, 3, 1, 72, 566, 43]
blist = mergesort(alist)
print(blist)