import random

def partition(a, left, right):
    p = random.randint(left, right)
    if p != left:
        a[left], a[p] = a[p], a[left]
    i = left + 1
    j = right
    done = False
    while not done:
        while i <= j and a[i] <= a[left]: i += 1
        while i <= j and a[j] >= a[left]: j -= 1

        if i > j:
            done = True
        else:
            a[i], a[j] = a[j], a[i]

    a[left], a[j] = a[j], a[left]
    return j


def quicksort(a, left, right):
    if left < right:
        p = partition(a, left, right)
        quicksort(a, left, p - 1)
        quicksort(a, p + 1, right)

a = [24, 2, 36, 77, 9, 0, 63, 5]
quicksort(a, 0, len(a)-1)
print(a)

