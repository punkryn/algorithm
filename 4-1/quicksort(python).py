import random

def qsort(a):
    less = []
    equal = []
    greater = []
    if len(a) > 1:
        pivot = a[random.randrange(0, len(a))]
        for x in a:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        print(less, equal, greater)
        return qsort(less) + equal + qsort(greater)
    else:
        return a

a = [24, 2, 36, 77, 9, 0, 63, 5]
b = qsort(a)
print(b)

