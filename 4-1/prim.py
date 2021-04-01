def setAdj(G):
    Adj = dict()
    for v in G['vertices']:
        Adj[v] = []
    for e in G['edges']:
        weight, u, v = e
        Adj[u].append(e)

    return Adj

def primMst(G, Adj):
    T = dict()
    Bound = []
    p = G['vertices'][0]
    T[p] = "start"

    while len(T) < len(G['vertices']):
        for e in Adj[p]:
            w, p, u = e
            if u in T:
                Bound.remove((w, u, p))
            else:
                Bound.append(e)
        mine = min(Bound, key=lambda x: x[0])
        p = mine[2]
        T[p] = mine

    return T

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'edges': [
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
    ]
}
Adj = setAdj(graph)
print(primMst(graph, Adj))



