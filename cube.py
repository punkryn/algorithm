# 2 5 4 6 1 3 6 2 5 5 1 2 3 5 3 1 1 2 4 6 6 4 3 4

# https://www.acmicpc.net/problem/16939


from sys import stdin

def statecheck(now):
    check = True
    for i in range(1, 7):
        color = now[i * 4 - 3]
        for j in range((i * 4) - 3, (i * 4) + 1):
            if color != now[j]:
                check = False
                break
        if not check:
            break

    return check

def rightclock(now):
    index = [2, 4, 6, 8, 10, 12, 23, 21]
    color = []

    for i in index:
       color.append(now[i])

    index = (index[2:] + index[:2])

    for i in index:
        c = color.pop(0)
        now[i] = c

def rightrev(now):
    index = [2, 4, 6, 8, 10, 12, 23, 21]
    color = []

    for i in index:
        color.append(now[i])

    length = len(index)
    index = (index[length-2:] + index[:length-2])

    for i in index:
        c = color.pop(0)
        now[i] = c

def leftclock(now):
    index = [1, 3, 5, 7, 9, 11, 24, 22]
    color = []

    for i in index:
        color.append(now[i])

    index = (index[2:] + index[:2])

    for i in index:
        c = color.pop(0)
        now[i] = c

def leftrev(now):
    index = [1, 3, 5, 7, 9, 11, 24, 22]
    color = []

    for i in index:
        color.append(now[i])

    length = len(index)
    index = (index[length-2:] + index[:length-2])

    for i in index:
        c = color.pop(0)
        now[i] = c

def frontclock(now):
    index = [7, 8, 19, 20, 23, 24, 16, 15]
    color = []

    for i in index:
        color.append(now[i])

    length = len(index)
    index = (index[2:] + index[:2])

    for i in index:
        c = color.pop(0)
        now[i] = c

def frontrev(now):
    index = [7, 8, 19, 20, 23, 24, 16, 15]
    color = []

    for i in index:
        color.append(now[i])

    length = len(index)
    index = (index[length - 2:] + index[:length - 2])

    for i in index:
        c = color.pop(0)
        now[i] = c

def backclock(now):
    index = [5, 6, 17, 18, 21, 22, 13, 14]
    color = []

    for i in index:
        color.append(now[i])

    index = (index[2:] + index[:2])

    for i in index:
        c = color.pop(0)
        now[i] = c

def backrev(now):
    index = [5, 6, 17, 18, 21, 22, 13, 14]
    color = []

    for i in index:
        color.append(now[i])

    length = len(index)
    index = (index[length - 2:] + index[:length - 2])

    for i in index:
        c = color.pop(0)
        now[i] = c

def topclock(now):
    index = [1, 2, 18, 20, 12, 11, 15, 13]
    color = []

    for i in index:
        color.append(now[i])

    index = (index[2:] + index[:2])

    for i in index:
        c = color.pop(0)
        now[i] = c

def toprev(now):
    index = [1, 2, 18, 20, 12, 11, 15, 13]
    color = []

    for i in index:
        color.append(now[i])

    length = len(index)
    index = (index[length - 2:] + index[:length - 2])

    for i in index:
        c = color.pop(0)
        now[i] = c

def bottomclock(now):
    index = [3, 4, 17, 19, 12, 11, 16, 14]
    color = []

    for i in index:
        color.append(now[i])

    index = (index[2:] + index[:2])

    for i in index:
        c = color.pop(0)
        now[i] =c

def bottomrev(now):
    index = [3, 4, 17, 19, 12, 11, 16, 14]
    color = []

    for i in index:
        color.append(now[i])

    length = len(index)
    index = (index[length-2:] + index[:length-2])

    for i in index:
        c = color.pop(0)
        now[i] = c

cube = list(map(int, stdin.readline().split()))

red = 1
blue = 2
green = 3
purple = 4
yellow = 5
grey = 6

# 회전하는 경우의 수는 전 후 좌 우에서 시계 방향과 시계 반대 방향
length = len(cube)
now = [0] * (len(cube) + 1)
for i in range(1, length + 1):
    now[i] = cube[i - 1]

checklist = []

rightclock(now)
check = statecheck(now)
rightrev(now)
checklist.append(check)

leftclock(now)
check = statecheck(now)
leftrev(now)
checklist.append(check)

frontclock(now)
check = statecheck(now)
frontrev(now)
checklist.append(check)

backclock(now)
check = statecheck(now)
backrev(now)
checklist.append(check)

rightrev(now)
check = statecheck(now)
rightclock(now)
checklist.append(check)

leftrev(now)
check = statecheck(now)
leftclock(now)
checklist.append(check)

frontrev(now)
check = statecheck(now)
frontclock(now)
checklist.append(check)

backrev(now)
check = statecheck(now)
backclock(now)
checklist.append(check)

topclock(now)
check = statecheck(now)
toprev(now)
checklist.append(check)

toprev(now)
check = statecheck(now)
topclock(now)
checklist.append(check)

bottomclock(now)
check = statecheck(now)
bottomrev(now)
checklist.append(check)

bottomrev(now)
check = statecheck(now)
bottomclock(now)
checklist.append(check)

#print(now)
#print(checklist)

if True in checklist:
    print(1)
else:
    print(0)
