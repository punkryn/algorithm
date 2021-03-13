# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

# distance answer: [1000000000, 0, 2, 3, 1, 2, 4]

INF = int(1e9)

import heapq

n, m = map(int, input().split())

start = int(input())

distance = [INF] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dis, node = heapq.heappop(q)

        if distance[node] < dis:
            continue

        for item in graph[node]:
            cost = dis + item[1]
            if distance[item[0]] > cost:
                distance[item[0]] = cost
                heapq.heappush(q, (cost, item[0]))

dijkstra(start)

print(distance)