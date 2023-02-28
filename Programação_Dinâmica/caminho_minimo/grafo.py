NOT = -1
INF = 99999

graph_incidence = {
    1: {1: 0},
    2: {1: 3},
    3: {1: 7},
    4: {1: 9},
    5: {2: 11, 3: 2, 4: 1},
    6: {2: 7, 3: 9, 4: 9},
    7: {5: 8, 6: 2},
}

z = {1: 0, 2: INF, 3: INF, 4: INF, 5: INF, 6: INF, 7: INF}

INIT = 0


for v in graph_incidence:
    d = INF
    for u in graph_incidence[v]:
        d = min(d, z[u] + graph_incidence[v][u])
    z[v] = d

print(z)

k = {1: 0, 2: INF, 3: INF, 4: INF, 5: INF, 6: INF, 7: INF}

graph_adjacence = {
    1: {2: 3, 3: 7, 4: 9},
    2: {5: 11, 6: 7},
    3: {5: 2, 6: 9},
    4: {5: 1, 6: 9},
    5: {7: 8},
    6: {7: 2},
    7: {},
}

for u in graph_adjacence:
    d = INF
    for v in graph_adjacence[u]:
        k[v] = min(k[v], graph_adjacence[u][v] + k[u])

print(k)
