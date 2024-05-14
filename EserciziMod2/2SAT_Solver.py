from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, stack)
        stack.append(v)

    def transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def scc_util(self, v, visited, result):
        visited[v] = True
        result.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.scc_util(i, visited, result)

    def get_scc(self):
        stack = []
        visited = [False] * (self.V + 1)  # Aggiunto 1 per evitare out of range
        for i in range(1, self.V + 1):  # Aggiunto 1 per evitare out of range
            if not visited[i]:
                self.dfs(i, visited, stack)

        gr = self.transpose()

        visited = [False] * (self.V + 1)  # Aggiunto 1 per evitare out of range
        scc_list = []
        while stack:
            i = stack.pop()
            if not visited[i]:
                result = []
                gr.scc_util(i, visited, result)
                scc_list.append(result)
        return scc_list


def is_2sat_satisfiable(n, clauses):
    g = Graph(2 * n)
    for clause in clauses:
        u, v = clause[0], clause[1]
        if u > 0 and v > 0:
            g.add_edge(u + n, v)
            g.add_edge(v + n, u)
        elif u > 0 and v < 0:
            g.add_edge(u + n, -v + n)
            g.add_edge(-v, u)
        elif u < 0 and v > 0:
            g.add_edge(-u, v)
            g.add_edge(v + n, -u + n)
        else:
            g.add_edge(-u, -v + n)
            g.add_edge(-v, -u + n)

    scc = g.get_scc()

    for component in scc:
        for vertex in component:
            if vertex + n in component:
                return False
    return True


# Esempio di utilizzo
n = 3  # Numero di variabili
clauses = [(1, 2), (-1, -2), (1, -2), (-1, 2)]  # Clauses della CNF formula

if is_2sat_satisfiable(n, clauses):
    print("La formula è soddisfacibile.")
else:
    print("La formula non è soddisfacibile.")
