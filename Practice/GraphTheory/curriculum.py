# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

from collections import deque

n = int(input())

indegree = [0] * (n + 1)
costList = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    tmp = map(int, input().split())
    cost = 0
    sub = []
    for j, item in enumerate(tmp):
        if j == 0:
            cost = item
            costList[i] = cost
        elif item != -1:
            graph[item].append((i, cost))
            indegree[i] += 1

print(graph)
print(indegree)

start = 0
for i in range(1, n + 1):
    if indegree[i] == 0:
        start = i
        break

q = deque()
q.append(start)
time = costList[start]
count = 1
#print(time)
result = costList.copy()
while q:
    node = q.popleft()

    for item in graph[node]:
        next_way, cost = item
        indegree[next_way] -= 1
        #costList[next_way] = (costList[node] + costList[next_way])
        result[next_way] = max(result[next_way], result[node] + costList[next_way] )
        if indegree[next_way] == 0:
            q.append(next_way)

for i in range(1, n + 1):
    print(result[i])