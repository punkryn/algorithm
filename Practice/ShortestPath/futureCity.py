# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# 4 2
# 1 3
# 2 4
# 3 4

import heapq

INF = int(1e9)
n, m = map(int, input().split())

distance = [INF] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())

def dijkstra(start):
    q = []
    distance[start] = 0

    heapq.heappush(q, (0, start))

    while q:
        print(distance)
        dis, node = heapq.heappop(q)

        for item in graph[node]:
            cost = dis + item[1]
            if distance[item[0]] > cost:
                distance[item[0]] = cost
                heapq.heappush(q, (cost, item[0]))
result = 0
dijkstra(1)
result += distance[k]
print(distance)

distance = [INF] * (n + 1)
dijkstra(k)
result += distance[x]
print(distance)

if result >= INF:
    print(-1)
else:
    print(result)