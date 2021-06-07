parent = dict()
rank = dict()

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2

        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    print(edges)
    for edge in edges:
        weight, vertice1, vertice2 = edge
        #print(find(vertice1), find(vertice2), parent)
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)

    return sorted(minimum_spanning_tree)

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

graph = {
    'vertices': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    'edges': set([
        (3, '1', '4'), (3, '4', '1'),
        (2, '1', '3'), (2, '3', '1'),
        (3, '2', '3'), (3, '3', '2'),
        (2, '3', '4'), (2, '4', '3'),
        (1, '3', '6'), (1, '6', '3'),
        (1, '7', '6'), (1, '6', '7'),
        (4, '5', '6'), (4, '6', '5'),
        (1, '6', '9'), (1, '9', '6'),
        (2, '7', '8'), (2, '8', '7'),
        (1, '9', '10'), (1, '10', '9'),
        (4, '8', '10'), (4, '10', '8'),
        (4, '2', '7'), (4, '7', '2'),
        (4, '2', '4'), (4, '4', '2'),
        (4, '4', '6'), (4, '6', '4'),
        (4, '8', '9'), (4, '9', '8')
    ])
}

print(kruskal(graph))