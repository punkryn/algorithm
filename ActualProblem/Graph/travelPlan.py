# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3

n, m = map(int, input().split())

travel = [list(map(int, input().split())) for _ in range(n)]

spot = list(map(int, input().split()))

connect = [i for i in range(n + 1)]

def find(connect, x):
    if connect[x] == x:
        return x
    else:
        connect[x] = find(connect, connect[x])
        return connect[x]

def union(connect, x, y):
    x = find(connect, x)
    y = find(connect, y)

    if x < y:
        connect[y] = x
    else:
        connect[x] = y

for i in range(n):
    for j in range(n):
        if travel[i][j] == 1:
            union(connect, i + 1, j + 1)

check = False
for i in range(m - 1):
    if connect[spot[i]] != connect[spot[i + 1]]:
        check = True

if check:
    print('NO')
else:
    print('YES')