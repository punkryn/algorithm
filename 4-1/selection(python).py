import random

def partition(a):
    less = []
    equal = []
    greater = []
    pivot = a[random.randrange(0, len(a))]
    for x in a:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    return less, equal, greater

def selection(a, k):
    less, equal, greater = partition(a)
    if k <= len(less):
        return selection(less, k)
    elif k == len(less) + len(equal):
        return equal[0]
    else:
        return selection(greater, k - len(less) - 1)

a = [24, 2, 36, 77, 9, 0, 63, 5]
v = selection(a, 4)
print(v)
