# Python3 program for Bellman-Ford's single source
# shortest path algorithm.

# Class to represent a graph
from colorama import Fore, Style

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # utility function used to print the solution
    def printArr(self, dist, src):
        print("Vertex Distance from Source = {0}".format(src))
        for i in range(self.V):
            print("To {0}\t\u2192\t{1}".format(i, dist[i]))

    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm. The function
    # also detects negative weight cycle
    def BellmanFord(self, src):
        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print(Fore.RED + "[Error] "+ Style.RESET_ALL+"Graph contains negative weight cycle")
                return

        # print all distance
        self.printArr(dist, src)


# Driver's code
if __name__ == "__main__":
    # x = int(input("Number of nodes : "))
    y = int(input("Choose Source Vertex : "))
    if y > 5: #in this case 5 is a costant, but here we put n = number of nodes
        print(Fore.RED+"[Error] "+Style.RESET_ALL+"in input source vertex")
        exit()
    g = Graph(5)
    
    print(
        Fore.GREEN + "[Info] " +Style.RESET_ALL+"Nota bene, il grafo  che verrà analizzato è quello delle slide di Guala, solo con gli archi invertiti"
    )
    print(
        Fore.GREEN + "[Info] " +Style.RESET_ALL+"Questo algoritmo considera anche i cicli negativi"
    )
    g.addEdge(0, 3, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(3, 2, 3)
    g.addEdge(3, 4, 2)
    g.addEdge(3, 1, 2)
    g.addEdge(1, 3, 1)
    g.addEdge(1, 2, 5)
    g.addEdge(4, 1, -3)

    # function call
    g.BellmanFord(y)
