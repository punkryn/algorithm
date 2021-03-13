# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4

import heapq
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, start)

    while q:
        cost, node = heapq.heappop(q)

        if cost > distance[node]:
            continue

        for item in graph[node]:
            index, dis = item
            if dis + cost < distance[index]:
                distance[index] = (dis + cost)
                heapq.heappush(q, (dis + cost, index))

for _ in range(int(input())):
    n = int(input())

    space = [list(map(int, input().split())) for _ in range(n)]
    #print(space)

    numbering = [[] for _ in range(n)]
    count = 1
    for i in range(n):
        for j in range(n):
            numbering[i].append(count)
            count += 1

    #print(numbering)

    distance = [INF] * (n**2 + 1)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    graph = [[] for _ in range((n ** 2) + 1)]

    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                if 0 <= ni < n and 0 <= nj < n:
                    #print(ni, nj)
                    graph[numbering[i][j]].append((numbering[ni][nj], space[ni][nj]))

    #print(graph)

    distance[1] = space[0][0]

    dijkstra((space[0][0], 1))

    #print('distance', distance)
    print(distance[n ** 2])