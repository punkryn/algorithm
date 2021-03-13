# 3 3
# 1 2
# 1 3
# 2 3

def find_root(parents, n):
    if parents[n] == n:
        return parents[n]
    else:
        parents[n] = find_root(parents, parents[n])
        return parents[n]

def union_parent(parents, a, b):
    a = find_root(parents, a)
    b = find_root(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

e, v = map(int, input().split())

parents = [i for i in range(e + 1)]

cycle = False

for _ in range(v):
    a, b = map(int, input().split())

    if find_root(parents, a) == find_root(parents, b):
        cycle = True
        break
    else:
        union_parent(parents, a, b)

if cycle:
    print('cycle')
else:
    print('not cycle')

