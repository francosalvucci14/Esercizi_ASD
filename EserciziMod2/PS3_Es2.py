def max_score(scores):
    n = len(scores[0])
    if n == 0:
        return 0

    # Inizializzazione dei primi tre valori
    dp = [0] * n
    dp[0] = max(scores[0][0], scores[1][0])
    if n > 1:
        dp[1] = max(dp[0], max(scores[0][1], scores[1][1]))
    if n > 2:
        dp[2] = max(dp[1], max(scores[0][2] + dp[0], scores[1][2] + dp[0]))

    # Calcolo dei massimi punteggi per ogni colonna
    for j in range(3, n):
        # Massimo punteggio scegliendo di posizionare una pedina nella colonna j
        max_score_j = max(
            scores[0][j] + max(dp[j - 2], dp[j - 3]),
            scores[1][j] + max(dp[j - 2], dp[j - 3]),
        )
        dp[j] = max(dp[j - 1], max_score_j)

    return dp[-1]


# Esempio di utilizzo
scores = [
    [3, 10, 10, 15, 6, 5, 30, 2, 1],
    [7, 2, 10, 1, 1, 2, 1, 3, 1000],
    [1, 5, 8, 12, 30, 6, 30, 4, 1],
]
print(max_score(scores))  # Output atteso: 1139
