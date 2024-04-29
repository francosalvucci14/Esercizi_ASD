def max_score_with_skip(colors):
    n = len(colors)
    if n == 0:
        return 0
    elif n == 1:
        return max(colors[0])  # Se c'è solo una pedina, restituisce il massimo dei suoi punteggi
    
    DP = [0] * (n + 1)  # Inizializzazione del vettore dei punteggi dinamici
    DP[1] = colors[0][0]  # Il punteggio per la prima posizione
    
    for i in range(2, n + 1):
        # Calcola il punteggio massimo fino alla posizione i
        DP[i] = max(
            DP[i-1] + colors[i-1][0],  # Piazzando una pedina bianca
            DP[i-2] + colors[i-1][1],  # Piazzando una pedina grigia
            DP[i-3] + colors[i-1][2],  # Piazzando una pedina nera
            DP[i-1] if i > 1 else 0  # Saltando la colonna corrente se possibile
        )

    return DP[n]

# Esempio di utilizzo:
colors = [(3, 7, 1), (2, 1, 5), (5, 3, 2), (4, 6, 8)]  # Esempio di colori
print("Massimo punteggio ottenibile con possibilità di saltare una colonna:", max_score_with_skip(colors))
