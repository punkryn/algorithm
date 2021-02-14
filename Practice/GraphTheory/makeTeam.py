# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

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

n, m = map(int, input().split())

parents = [i for i in range(n + 1)]
result = []
for _ in range(m):
    c, a, b = map(int, input().split())

    if c == 0:
        union_parent(parents, a, b)
    elif c == 1:
        if find_root(parents, a) == find_root(parents, b):
            result.append('YES')
        else:
            result.append('NO')

for ans in result:
    print(ans)