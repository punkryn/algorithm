# def mergesort(arr):
#     if len(arr) < 2:
#         return arr
#
#     mid = len(arr) // 2
#     low_arr = mergesort(arr[:mid])
#     high_arr = mergesort(arr[mid:])
#     #print(low_arr, high_arr)
#
#     merged_arr = []
#     l = h = 0
#     while l < len(low_arr) and h < len(high_arr):
#         if low_arr[l] < high_arr[h]:
#             merged_arr.append(low_arr[l])
#             l += 1
#         else:
#             merged_arr.append(high_arr[h])
#             h += 1
#     merged_arr += low_arr[l:]
#     merged_arr += high_arr[h:]
#
#     return merged_arr
#
#
# alist = [4, 26, 9, 3, 1, 72, 566, 43]
# blist = mergesort(alist)
# print(blist)
#


def mergesort(a):
    if len(a) > 1:
        k = (len(a) - 1) // 2
        return merge(mergesort(a[:k+1]), mergesort(a[k+1:]))
    else:
        return a

def merge(a, b):
    c = []

    while a and b:
        aele = a.pop(0)
        bele = b.pop(0)

        if aele > bele:
            c.append(bele)
            a.insert(0, aele)
        elif aele < bele:
            c.append(aele)
            b.insert(0, bele)
        else:
            c.append(aele)
            c.append(bele)

    return c + a + b

alist = [4, 26, 9, 3, 1, 72, 566, 43]
blist = mergesort(alist)
print(blist)
