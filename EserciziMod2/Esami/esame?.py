# Stampa Matrice
def printMatrix(M):
    # Trova il numero massimo di cifre in ciascun elemento della matrice
    max_length_per_column = [len(str(max(col, key=abs))) for col in zip(*M)]

    for row in M:
        for col, element in enumerate(row):
            padding = max_length_per_column[col] - len(str(element))
            left_padding = padding // 2
            right_padding = padding - left_padding
            print(" " * left_padding + str(element) + " " * right_padding, end="  ")
        print()
    print()


def massimo_guadagno1(n, ai, bi):
    if n == 0:
        return 0
    elif n == 1:
        return max(ai[0], bi[0])

    # Inizializzazione delle tabelle dp
    dp = [0] * n

    # Inizializzazione dei casi base
    dp[0] = max(ai[0], bi[0])
    if n > 1:
        dp[1] = max(ai[0] + ai[1], bi[1])

    # Riempimento della tabella dp
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 1] + ai[i])
        if i >= 2:
            dp[i] = max(dp[i], dp[i - 2] + bi[i])
        if i >= 3:
            dp[i] = max(dp[i], dp[i - 3] + bi[i])

    # Il massimo guadagno sarà dp[n-1]
    return dp[n - 1]


def massimo_guadagno(n, ai, bi):
    OPT = [[0] * 2 for _ in range(n)]

    OPT[0][0] = 0
    OPT[0][1] = 0

    for i in range(1, n):
        OPT[i][0] = max(ai[i] + OPT[i - 1][1], OPT[i - 2][0] + bi[i])
        OPT[i][1] = max(ai[i] + OPT[i - 1][1], OPT[i - 3][0] + bi[i - 1])
    printMatrix(OPT)
    return max(OPT[n - 1][0], OPT[n - 1][1])


a = [10, 20, 30, 40, 50]
b = [15, 25, 35, 45, 55]
n = len(a)
totale = massimo_guadagno(n, a, b)
print(totale)

print(massimo_guadagno1(n, a, b))
