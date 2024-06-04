import heapq
from colorama import Fore, Style


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dijkstra(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        min_heap = [(0, src)]

        while min_heap:
            d, u = heapq.heappop(min_heap)
            if d > dist[u]:
                continue
            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(min_heap, (dist[v], v))
        return dist


# Esempio di utilizzo
if __name__ == "__main__":
    g = Graph(50)
    # Aggiungi tutti gli archi del grafo
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 15)
    g.add_edge(1, 3, 7)
    g.add_edge(1, 4, 20)
    g.add_edge(2, 5, 25)
    g.add_edge(2, 6, 5)
    g.add_edge(3, 7, 12)
    g.add_edge(3, 8, 9)
    g.add_edge(4, 9, 11)
    g.add_edge(4, 10, 8)
    g.add_edge(5, 11, 13)
    g.add_edge(5, 12, 17)
    g.add_edge(6, 13, 6)
    g.add_edge(6, 14, 14)
    g.add_edge(7, 15, 19)
    g.add_edge(7, 16, 4)
    g.add_edge(8, 17, 21)
    g.add_edge(8, 18, 3)
    g.add_edge(9, 19, 16)
    g.add_edge(9, 20, 22)
    g.add_edge(10, 21, 18)
    g.add_edge(10, 22, 23)
    g.add_edge(11, 23, 26)
    g.add_edge(11, 24, 27)
    g.add_edge(12, 25, 30)
    g.add_edge(12, 26, 28)
    g.add_edge(13, 27, 24)
    g.add_edge(13, 28, 29)
    g.add_edge(14, 29, 32)
    g.add_edge(14, 30, 31)
    g.add_edge(15, 31, 35)
    g.add_edge(15, 32, 36)
    g.add_edge(16, 33, 33)
    g.add_edge(16, 34, 34)
    g.add_edge(17, 35, 38)
    g.add_edge(17, 36, 37)
    g.add_edge(18, 37, 40)
    g.add_edge(18, 38, 39)
    g.add_edge(19, 39, 42)
    g.add_edge(19, 40, 41)
    g.add_edge(20, 41, 44)
    g.add_edge(20, 42, 43)
    g.add_edge(21, 43, 47)
    g.add_edge(21, 44, 45)
    g.add_edge(22, 45, 48)
    g.add_edge(22, 46, 46)
    g.add_edge(23, 47, 49)
    g.add_edge(23, 48, 50)
    g.add_edge(24, 49, 51)
    g.add_edge(24, 0, 52)
    g.add_edge(25, 1, 53)
    g.add_edge(25, 2, 54)
    g.add_edge(26, 3, 55)
    g.add_edge(26, 4, 56)
    g.add_edge(27, 5, 57)
    g.add_edge(27, 6, 58)
    g.add_edge(28, 7, 59)
    g.add_edge(28, 8, 60)
    g.add_edge(29, 9, 61)
    g.add_edge(29, 10, 62)
    g.add_edge(30, 11, 63)
    g.add_edge(30, 12, 64)
    g.add_edge(31, 13, 65)
    g.add_edge(31, 14, 66)
    g.add_edge(32, 15, 67)
    g.add_edge(32, 16, 68)
    g.add_edge(33, 17, 69)
    g.add_edge(33, 18, 70)
    g.add_edge(34, 19, 71)
    g.add_edge(34, 20, 72)
    g.add_edge(35, 21, 73)
    g.add_edge(35, 22, 74)
    g.add_edge(36, 23, 75)
    g.add_edge(36, 24, 76)
    g.add_edge(37, 25, 77)
    g.add_edge(37, 26, 78)
    g.add_edge(38, 27, 79)
    g.add_edge(38, 28, 80)
    g.add_edge(39, 29, 81)
    g.add_edge(39, 30, 82)
    g.add_edge(40, 31, 83)
    g.add_edge(40, 32, 84)
    g.add_edge(41, 33, 85)
    g.add_edge(41, 34, 86)
    g.add_edge(42, 35, 87)
    g.add_edge(42, 36, 88)
    g.add_edge(43, 37, 89)
    g.add_edge(43, 38, 90)
    g.add_edge(44, 39, 91)
    g.add_edge(44, 40, 92)
    g.add_edge(45, 41, 93)
    g.add_edge(45, 42, 94)
    g.add_edge(46, 43, 95)
    g.add_edge(46, 44, 96)
    g.add_edge(47, 45, 97)
    g.add_edge(47, 46, 98)
    g.add_edge(48, 47, 99)
    g.add_edge(48, 48, 100)
    g.add_edge(49, 49, 101)
    g.add_edge(49, 0, 102)

    # # Esegui l'algoritmo di Dijkstra per il nodo di partenza 0
    # # Trova le distanze da src a tutti i nodi
    # src = 0
    # distances = g.dijkstra(src)
    # print(Fore.GREEN+"[INFO] "+Style.RESET_ALL+"Algoritmo di Dijkstra con sorgente {} verso tutti i nodi".format(src))
    # for i in range(len(distances)):
    #     print("Da sorgente",src,"Al Nodo", i, "-> Distanza:", distances[i])

    # Esegui l'algoritmo di Dijkstra per la sorgente (ad esempio, il nodo 0) al nodo pozzo (indice 50)

    # src = 49
    src = int(input("Scegli nodo sorgente [0-49]: "))
    distances = g.dijkstra(src)
    sink = int(input("Scegli nodo pozzo [0-49]: "))
    print(
        Fore.GREEN
        + "[INFO] "
        + Style.RESET_ALL
        + "Algoritmo di Dijkstra con sorgente {} e pozzo {}".format(src, sink)
    )
    if sink == 50:
        print(
            "Distanza minima da nodo",
            src,
            "a nodo pozzo",
            sink,
            ": " + Fore.RED + "{}".format(distances[sink - 1]),
        )
    else:
        print(
            "Distanza minima da nodo",
            src,
            "a nodo pozzo",
            sink,
            ": " + Fore.RED + "{}".format(distances[sink]),
        )
