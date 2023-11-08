from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, state):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append((v, state))

    def get_adjacent_edges(self, u):
        return self.adj_list.get(u, [])

def find_strategy_to_win(graph, s, t, B):
    queue = deque([(s, [])])
    visited = set()

    while queue:
        current_node, path = queue.popleft()
        if current_node == t:
            return path

        visited.add(current_node)

        for neighbor, state in graph.get_adjacent_edges(current_node):
            if neighbor not in visited and state == "on":
                new_path = path + [(current_node, neighbor)]
                queue.append((neighbor, new_path))

        if current_node in B:
            for neighbor, state in graph.get_adjacent_edges(current_node):
                if state == "on":
                    graph.add_edge(current_node, neighbor, "off")
                else:
                    graph.add_edge(current_node, neighbor, "on")

    return None

# Esempio di utilizzo
graph = Graph()
graph.add_edge(1, 2, "on")
graph.add_edge(2, 3, "off")
graph.add_edge(3, 4, "on")
graph.add_edge(4, 5, "on")
graph.add_edge(4, 6, "off")
graph.add_edge(6, 5, "off")
graph.add_edge(2, 6, "off")
graph.add_edge(6, 2, "on")

start_node = 1
end_node = 5
special_buttons = {2, 4}

strategy = find_strategy_to_win(graph, start_node, end_node, special_buttons)
if strategy:
    print("Strategia per vincere il livello:", strategy)
else:
    print("Non esiste una strategia per vincere il livello.")
