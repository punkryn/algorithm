# parent = dict()
# rank = dict()
#
# def find(vertice):
#     if parent[vertice] != vertice:
#         parent[vertice] = find(parent[vertice])
#     return parent[vertice]
#
# def union(vertice1, vertice2):
#     root1 = find(vertice1)
#     root2 = find(vertice2)
#
#     if root1 != root2:
#         if rank[root1] > rank[root2]:
#             parent[root2] = root1
#         else:
#             parent[root1] = root2
#
#         if rank[root1] == rank[root2]:
#             rank[root2] += 1
#
# def make_set(vertice):
#     parent[vertice] = vertice
#     rank[vertice] = 0
#
# def kruskal(graph):
#     for vertice in graph['vertices']:
#         make_set(vertice)
#
#     minimum_spanning_tree = set()
#     edges = list(graph['edges'])
#     edges.sort()
#
#     for edge in edges:
#         weight, vertice1, vertice2 = edge
#         if find(vertice1) != find(vertice2):
#             union(vertice1, vertice2)
#             minimum_spanning_tree.add(edge)
#
#     return sorted(minimum_spanning_tree)
#
# graph = {
#     'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
#     'edges': set([
#         (13, 'A', 'J'), (13, 'J', 'A'),
#         (1, 'B', 'I'), (1, 'I', 'B'),
#         (375, 'C', 'H'), (375, 'H', 'C'),
#         (53, 'D', 'G'), (53, 'G', 'D'),
#         (875, 'E', 'F'), (875, 'F', 'E'),
#         (71, 'J', 'B'), (71, 'B', 'J'),
#         (17, 'I', 'C'), (17, 'C', 'I'),
#         (35, 'H', 'D'), (35, 'D', 'H'),
#         (756, 'G', 'E'), (756, 'E', 'G'),
#         (9, 'F', 'A'), (9, 'A', 'F'),
#         (246, 'C', 'J'), (246, 'J', 'C'),
#         (126, 'D', 'I'), (126, 'I', 'D'),
#         (136, 'E', 'H'), (136, 'H', 'E'),
#         (85, 'F', 'G'), (85, 'G', 'F'),
#         (163, 'D', 'J'), (163, 'J', 'D'),
#         (864, 'E', 'I'), (864, 'I', 'E'),
#         (126, 'F', 'H'), (126, 'H', 'F'),
#         (88, 'E', 'J'), (88, 'J', 'E'),
#         (64, 'F', 'I'), (64, 'I', 'F'),
#         (99, 'G', 'H'), (99, 'H', 'G')
#     ])
# }
#
# print(kruskal(graph))
#
#
#

parent = dict()
rank = dict()

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    r1 = find(v1)
    r2 = find(v2)

    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r2] = r1
        else:
            parent[r1] = r2

        if rank[r1] == rank[r2]:
            rank[r1] += 1

def make_set(v):
    parent[v] = v
    rank[v] = 0

def kruskal(graph):
    for v in graph['vertices']:
        make_set(v)

    mst = set()
    edges = list(graph['edges'])
    edges.sort()

    for edge in edges:
        cost, v1, v2 = edge
        if find(v1) != find(v2):
            union(v1, v2)
            mst.add(edge)

    return sorted(mst)

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'edges': set([
        (13, 'A', 'J'), (13, 'J', 'A'),
        (1, 'B', 'I'), (1, 'I', 'B'),
        (375, 'C', 'H'), (375, 'H', 'C'),
        (53, 'D', 'G'), (53, 'G', 'D'),
        (875, 'E', 'F'), (875, 'F', 'E'),
        (71, 'J', 'B'), (71, 'B', 'J'),
        (17, 'I', 'C'), (17, 'C', 'I'),
        (35, 'H', 'D'), (35, 'D', 'H'),
        (756, 'G', 'E'), (756, 'E', 'G'),
        (9, 'F', 'A'), (9, 'A', 'F'),
        (246, 'C', 'J'), (246, 'J', 'C'),
        (126, 'D', 'I'), (126, 'I', 'D'),
        (136, 'E', 'H'), (136, 'H', 'E'),
        (85, 'F', 'G'), (85, 'G', 'F'),
        (163, 'D', 'J'), (163, 'J', 'D'),
        (864, 'E', 'I'), (864, 'I', 'E'),
        (126, 'F', 'H'), (126, 'H', 'F'),
        (88, 'E', 'J'), (88, 'J', 'E'),
        (64, 'F', 'I'), (64, 'I', 'F'),
        (99, 'G', 'H'), (99, 'H', 'G')
    ])
}

print(kruskal(graph))










































