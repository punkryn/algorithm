# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

def find_root(parents, n):
    #print('n, parents[n]', n, parents[n])
    if parents[n] == n:
        #print(parents)
        return parents[n]
    else:
        parents[n] = find_root(parents, parents[n])
        return parents[n]

def union_parents(parents, a, b):
    #print(a, b)
    a = find_root(parents, a)
    b = find_root(parents, b)
    #print(a, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

n, m = map(int, input().split())

parents = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    union_parents(parents, a, b)

for i in range(1, n + 1):
    print(find_root(parents, i), end=' ')

print()

for i in range(1, n + 1):
    print(parents[i], end=' ')


