import random

def partition(a, left, right):
    p = random.randint(left, right)
    if p != left:
        a[p], a[left] = a[left], a[p]

    i = left + 1
    j = right
    pvalue = a[left]
    done = False

    while not done:
        while i <= j and a[i] <= pvalue: i += 1
        while i <= j and a[j] >= pvalue: j -= 1

        if i > j:
            done = True
        else:
            a[i], a[j] = a[j], a[i]

    a[j], a[left] = a[left], a[j]
    return j

def selection(a, left, right, k):
    p = partition(a, left, right)
    s = (p - 1) - left + 1
    if s >= k:
        return selection(a, left, p-1, k)
    elif s + 1 == k:
        return a[p]
    else:
        return selection(a, p+1, right, k - s - 1)



a = [24, 2, 36, 77, 9, 0, 63, 5]
v = selection(a, 0, len(a)-1, 4)
print(v)





























