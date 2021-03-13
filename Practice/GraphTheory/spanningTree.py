# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25

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

graph = []

for _ in range(v):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

print(graph)

result = 0
while graph:
    cost, a, b = graph.pop(0)
    if find_root(parents, a) == find_root(parents, b):
        continue
    else:
        union_parent(parents, a, b)
        result += cost

print(result)