from collections import deque

# def bfs(graph, queue, b, visited):
#     visited[b] = True
#     while queue:
#         i = queue.popleft()
#         print(b, end=' ')
#         for j in graph[i]:
#             if not visited[j]:
#                 queue.append(j)
#                 visited[j] = True
#         bfs(graph, queue, i, visited)
#
#
# graph = [
#         [],
#         [2, 3, 8],
#         [1, 7],
#         [1, 4, 5],
#         [3, 5],
#         [3, 4],
#         [7],
#         [2, 6, 8],
#         [1, 7]
# ]
#
# visited = [False] * 9
#
# queue = deque()
# queue.append(1)
#
# bfs(graph, queue, 1, visited)

def bfs(graph, start, visited):

    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)