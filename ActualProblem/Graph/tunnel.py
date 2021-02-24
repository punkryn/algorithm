# 5
# 11 -15 -15
# 14 -5 -15
# -1 -1 -5
# 10 -4 -1
# 19 -4 19

# https://www.acmicpc.net/problem/2887

def find(parent, a):
    if parent[a] == a:
        return parent[a]
    else:
        parent[a] = find(parent, parent[a])
        return parent[a]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n = int(input())

x = []
y = []
z = []

parent = [i for i in range(n + 1)]

for i in range(1, n + 1):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

edges = []

for i in range(n - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort()

result = 0
count = 0
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
        count += 1

    if count == n - 1:
        break

print(result)