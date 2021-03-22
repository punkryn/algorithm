import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def brute(ax):
    mi = dist(ax[0], ax[1])
    p1 = ax[0]
    p2 = ax[1]
    ln_ax = len(ax)
    if ln_ax == 2:
        return p1, p2, mi

    for i in range(ln_ax-1):
        for j in range(i + 1, ln_ax):
            if i != 0 and j != 1:
                d = dist(ax[i], ax[j])
                if d < mi:
                    mi = d
                    p1, p2 = ax[i], ax[j]

    return p1, p2, mi

def closest_split_pair(p_x, p_y, delta, best_pair):
    ln_x = len(p_x)
    mx_x = p_x[ln_x // 2][0]

    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
    best = delta
    ln_y = len(s_y)
    for i in range(ln_y - 1):
        for j in range(i + 1, min(i + 8, ln_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst

    return best_pair[0], best_pair[1], best

def closest_pair(ax, ay):
    ln_ax = len(ax)
    if ln_ax <= 3:
        return brute(ax)
    mid = ln_ax // 2
    Qx = ax[:mid]
    Rx = ax[mid:]

    midpoint = ax[mid][0]
    Qy = list()
    Ry = list()

    for x in ay:
        if x[0] < midpoint:
            Qy.append(x)
        else:
            Ry.append(x)
    #print(Qy, Ry)
    (p1, q1, mi1) = closest_pair(Qx, Qy)
    (p2, q2, mi2) = closest_pair(Rx, Ry)

    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)

    (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)

    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3

def solution(x, y):
    a = list(zip(x, y))
    ax = sorted(a, key=lambda x: x[0])
    ay = sorted(a, key=lambda x: x[1])
    p1, p2, mi = closest_pair(ax, ay)
    print('best Pair', (p1, p2))
    return mi

xarr = [3, 8, 4, 11, 6, 6, 5, 1, 11, 10]
yarr = [3, 3, 6, 7, 6, 8, 1, 7, 1, 9]
dist = solution(xarr, yarr)
print("The shortest distance is", dist)
