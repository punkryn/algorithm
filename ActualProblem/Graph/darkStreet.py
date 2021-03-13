# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11

def find(parent, x):
    if parent[x] == x:
        return parent[x]
    else:
        parent[x] = find(parent, parent[x])
        return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().split())

# street = [[] for _ in range(n)]
# for _ in range(m):
#     x, y, z = map(int, input().split())
#     street[x].append((y, z))
#     street[y].append((x, z))

parent = [i for i in range(n)]
street = []
for _ in range(m):
    x, y, z = map(int, input().split())
    street.append((x, y, z))
    #union(parent, x, y)

street.sort(key=lambda x: x[2])
print(street)
print(parent)

result = 0
for info in street:
    x, y, cost = info

    if find(parent, x) == find(parent, y):
        result += cost
    else:
        union(parent, x, y)

print(parent)
print(result)
