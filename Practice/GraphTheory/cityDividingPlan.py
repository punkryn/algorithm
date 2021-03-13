# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4

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

graph = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

#print(graph)

graph.sort()

#print(graph)

max_cost = 0
result = 0
for item in graph:
    cost, a, b = item
    if find_root(parents, a) == find_root(parents, b):
        continue
    else:
        union_parent(parents, a, b)
        result += cost
        if cost > max_cost:
            max_cost = cost

print(result - max_cost)