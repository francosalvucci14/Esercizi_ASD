"""
Siete a bordo di una modernissima auto elettrica su un’autostrada. Entrate in autostrada al km 0 con la
batteria carica e dovete uscire al km L.
Prima che la vostra batteria si esaurisca (dopo r km), dovete fermarvi in un’area di servizio e sostituirla con
una batteria di ricambio.
Siano D[1 . . . n] e C[1 . . . n] due vettori di interi, dove D[i] `e la distanza dell’area di servizio i-isima
dall’inizio dell’autostrada, e C[i] `e il costo di una nuova batteria nell’area i.
Il costo totale del viaggio `e dato dalla somma dei costi delle batterie sostituite per arrivare al km N . Scrivete
un algoritmo che prenda in input N , r, n, D e C e restituisca il costo totale minimo. Discutere correttezza e
complessit`a.
Nota: Negli esercizi aggiuntivi del Capitolo 14 relativi alla tecnica greedy si trova una formulazione diversa
di questo problema
"""


def Batterie(D: list, C: list, n: int, r: int) -> int:

    OPT = [0] * (n + 1)
    OPT[n] = 0
    if r < D[0]:
        return f"Non si può cambiare batteria, in quanto i km di autonomia (ovvero r={r}) sono minoro della distanza dal km 0 al km {D[0]}"
    if r>max(D):
        return 0
    for i in range(n-1, -1, -1):
        j = i
        OPT[i] = float("inf")
        while j <= n and (D[j - 1] <= D[i - 1] + r):
            OPT[i] = min(OPT[i], OPT[j])
            j = j + 1
        OPT[i] = OPT[i] + C[i-1]
    print(OPT)
    return OPT[0]


D = [20, 40, 60]  
C = [10, 15, 20]
n = len(D)
r = 50
print(Batterie(D, C, n, r))
