import pprint as pp


def min_cost_traversal(costs, n, k):
    dp = [[float("inf")] * 2 for _ in range(n + 1)]
    dp[0][0] = dp[0][1] = 0
    #    pp.pprint(dp)
    for i in range(1, n + 1):
        for j in range(2):
            for x in range(2):
                if i == 1 or x == j:
                    dp[i][j] = min(dp[i][j], dp[i - 1][x] + costs[i - 1][j])
                else:
                    if k > 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][x] + costs[i - 1][j])
                        k -= 1
    # pp.pprint(dp)
    return min(dp[n][0], dp[n][1])


# Esempio di utilizzo
costs = [[1, 2], [5, 4], [5, 6], [2, 10]]  # Costi dei viaggi
n = len(costs)  # Numero di viaggi
k = 3  # Numero di cambi modalità disponibili
print("Istanza:")
pp.pprint(costs)
print("Il costo minimo della traversata è:", min_cost_traversal(costs, n, k))
