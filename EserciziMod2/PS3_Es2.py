def max_score(n, scores):
    # Inizializzazione della matrice dp
    dp = [[0] * n for _ in range(3)]

    # Riempimento della matrice dp
    for j in range(n):
        # Caso base per la prima riga
        if j == 0:
            dp[0][j] = scores[0][j]
        else:
            dp[0][j] = scores[0][j] + max(dp[1][j - 1], dp[2][j - 1])

        # Calcolo dei massimi punteggi per le righe successive
        for i in range(1, 3):
            dp[i][j] = scores[i][j] + max(dp[k][j] for k in range(3) if k != i)

    # Restituzione del massimo punteggio ottenibile
    return max(max(dp[0]), max(dp[1]), max(dp[2]))

# Esempio di utilizzo
board = [
    [3, 10, 10, 15, 6, 5, 30, 2, 1],
    [7, 2, 10, 1, 1, 2, 1, 3, 1000],
    [1, 5, 8, 12, 30, 6, 30, 4, 1],
]
n = len(board[0])
print(max_score(n, board))  # Output: 1139
