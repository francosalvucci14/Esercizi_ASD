from collections import defaultdict


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.row = len(graph)
        self.column = len(graph[0])

    def bfs(self, s, t, parent):
        visited = [False] * (self.row)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.row)
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


# Esempio di utilizzo
# g[i][j] = capacità dell'arco tra i e j
graph = [
    [0, 10, 10, 0, 0, 0],
    [0, 0, 2, 4, 8, 0],
    [0, 0, 0, 0, 9, 0],
    [0, 0, 0, 0, 0, 10],
    [0, 0, 0, 6, 0, 10],
    [0, 0, 0, 0, 0, 0],
]

g = Graph(graph)
source = 0
sink = 5
print("Algoritmo Ford-Fulkerson")
print("Il flusso massimo è: %d " % g.ford_fulkerson(source, sink))
