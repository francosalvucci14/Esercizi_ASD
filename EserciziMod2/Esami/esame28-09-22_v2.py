def max_votes(n, v, B):
    # Inizializzazione della matrice OPT
    OPT = [[0] * (B + 1) for _ in range(n)]

    # Base cases
    if B > 0:
        OPT[0][1] = v[0]
    else:
        return 0

    for i in range(1, n):
        for b in range(B + 1):
            OPT[i][b] = OPT[i - 1][b]  # Non facciamo un comizio il giorno i
            if b > 0 and i > 1:
                OPT[i][b] = max(OPT[i][b], OPT[i - 2][b - 1] + v[i])
            elif b > 0 and i == 1:
                OPT[i][b] = max(OPT[i][b], v[i])  # Caso speciale per il secondo giorno

    # Il risultato finale è il massimo numero di voti ottenibile considerando tutti i giorni e al massimo B comizi
    return max(OPT[n - 1][b] for b in range(B + 1))


# Esempio di utilizzo
# valori = [10, 2, 11, 10, 5]
valori = [1, 1, 1, 9, 10, 9, 1, 1, 8]
# valori = [9, 8, 1, 3]
B = 3
n = len(valori)
print(max_votes(n, valori, B))  # Output atteso: 30
