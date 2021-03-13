# 3 2 1
# 1 2 4
# 1 3 2

import heapq

INF = int(1e9)
n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

# visited = [0] * (n + 1)

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    #visited[start] = 1
    while q:
        #print(q)
        dis, node = heapq.heappop(q)

        for item in graph[node]:
            cost = dis + item[1]
            if distance[item[0]] > cost:
                distance[item[0]] = cost
                heapq.heappush(q, (cost, item[0]))
                # visited[item[0]] = 1

dijkstra(c)
count = 0
# for i in range(1, n + 1):
#     count += visited[i]

#print(distance)
time = 0
for i in range(1, n + 1):
    if distance[i] < INF:
        count += 1
        if distance[i] > time:
            time = distance[i]

print(count-1, time)