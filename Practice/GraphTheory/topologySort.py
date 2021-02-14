# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

def find_min_index():
    for i in range(1, v + 1):
        if indegree[i] == 0 and not visited[i]:
            return i


v, e = map(int, input().split())

indegree = [0] * (v + 1)
visited = [False] * (v + 1)
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

print(indegree)

q = []
start = find_min_index()
q.append(start)
visited[start] = True

while q:
    node = q.pop(0)
    print(node, end=' ')
    for item in graph[node]:
        indegree[item] -= 1
        if indegree[item] == 0 and not visited[item]:
            q.append(item)
            visited[item] = True

