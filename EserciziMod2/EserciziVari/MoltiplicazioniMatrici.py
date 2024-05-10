def matrix_chain_order(p):
    n = len(p) - 1  # Numero di matrici
    m = [[0] * n for _ in range(n)]  # Tabella per memorizzare i costi minimi
    s = [
        [0] * n for _ in range(n)
    ]  # Tabella per memorizzare i punti di divisione ottimali

    # Calcolo del costo minimo della moltiplicazione di catene di lunghezza 2, 3, ..., n
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        print("A" + str(i + 1), end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")


# Esempio di utilizzo
matrici = [10, 20, 30, 40]
m, s = matrix_chain_order(matrici)
print("Ordine Ottimale di Moltiplicazione:", end=" ")
print_optimal_parens(s, 0, len(matrici) - 2)
