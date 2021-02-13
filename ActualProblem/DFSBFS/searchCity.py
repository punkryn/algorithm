# https://acmicpc.net/problem/18352

#

from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

def bfs(start, end):
    q = deque()
    count = 1
    for item in graph[start]:
        q.append((item, count))

    while q:
        now = q.popleft()
        #print(now)

        if now[1] - 1 == end:
            return now[1]
        if distance[now[0]] == -1:
            if now[1] > count:
                count += 1
                distance[now[0]] = count

            else:
                distance[now[0]] = count

        if now[1] > end:
            return -1

        for item in graph[now[0]]:
            if distance[item] == -1:
                q.append((item, count + 1))

bfs(x, k)
#print(distance)
sw = False
for i, dis in enumerate(distance):
    if dis == k:
        sw = True
        print(i)

if not sw:
    print(-1)