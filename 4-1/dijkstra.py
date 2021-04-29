def dijkstra(g, adj, p):
    bound = []
    d = dict()
    d[p] = 0
    done = []
    done.append(p)
    while len(done) < len(g['vertices']):
        for e in adj[p]:
            w, u, v = e
            if v not in done:
                if v in d:
                    d[v] = min(d[v], d[p] + w)
                else:
                    d[v] = d[p] + w
                    bound.append(v)
        #print(d)
        # tmp = int(1e9)
        # vmin = ''
        # for v in bound:
        #     if d[v] < tmp:
        #         tmp = d[v]
        #         vmin = v
        vmin = min(bound, key=lambda x: d[x])
        #vmin = min(bound)
        print("bound: ", bound)
        print("vmin", vmin)
        bound.remove(vmin)
        done.append(vmin)
        p = vmin
    return d

def setAdj(G):
    Adj = dict()
    for v in G['vertices']:
        Adj[v] = []
    for e in G['edges']:
        weight, u, v = e
        Adj[u].append(e)

    return Adj

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
    'edges': [
        (2, 'A', 'B'), (2, 'B', 'A'),
        (8, 'A', 'C'), (8, 'C', 'A'),
        (18, 'A', 'D'), (18, 'D', 'A'),
        (3, 'B', 'C'), (3, 'C', 'B'),
        (9, 'C', 'D'), (9, 'D', 'C'),
        (2, 'B', 'E'), (2, 'E', 'B'),
        (7, 'B', 'F'), (7, 'F', 'B'),
        (9, 'C', 'F'), (9, 'F', 'C'),
        (4, 'D', 'F'), (4, 'F', 'D'),
        (3, 'E', 'F'), (3, 'F', 'E')
    ]
}
Adj = setAdj(graph)
print(dijkstra(graph, Adj, 'A'))