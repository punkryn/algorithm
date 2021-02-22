# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2

import heapq
INF = int(1e9)


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

distance[1] = 0

start = (0, 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

q = []
heapq.heappush(q, start)

while q:
    dis, node = heapq.heappop(q)

    if dis > distance[node]:
        continue

    for item in graph[node]:
        b, c = item
        cost = dis + c
        if cost < distance[b]:
            distance[b] = cost
            heapq.heappush(q, (cost, b))

hut = 0
for dis in distance:
    if dis == INF:
        continue
    if hut < dis:
        hut = dis

print(distance.index(hut), hut, distance.count(hut))