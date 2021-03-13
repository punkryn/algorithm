tmp = [i for i in range(10)]

start = 0
end = 9

mid = (start + end) // 2

while start < end:
    mid = (start + end) // 2
    print('start, end', start, end)
    if tmp[mid] > 3:
        end = mid - 1
    elif tmp[mid] < 3:
        start = mid + 1
    else:
        break

print(tmp[start], tmp[end], tmp[mid])


def bs(goal, start, end):
    mid = (start + end) // 2

    if start < end:
        if tmp[mid] > goal:
            return bs(goal, start, mid - 1)
        elif tmp[mid] < goal:
            return bs(goal, mid + 1, end)
        else:
            return tmp[start]
    return tmp[start]

print(bs(3, 0, 9))