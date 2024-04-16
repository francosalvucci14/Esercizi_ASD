import numpy as np
from colorama import Fore, Back, Style


def SeqAl(m, n, X, Y, delta, alpha):
    M = np.zeros((n + 1, m + 1), dtype=int)
    for i in range(n + 1):
        M[i][0] = i * delta
    for j in range(m + 1):
        M[0][j] = j * delta
    for i in range(1, n + 1):
        charX = X[i - 1][1]
        for j in range(1, m + 1):
            charY = Y[j - 1][1]

            M[i][j] = min(
                alpha[charY][charX] + M[i - 1][j - 1],
                delta + M[i - 1][j],
                delta + M[i][j - 1],
            )

    return M[n][m]


def SeqAlAlpha1(m, n, X, Y, delta, alpha):
    M = np.zeros((n + 1, m + 1), dtype=int)
    for i in range(n + 1):
        M[i][0] = i * delta
    for j in range(m + 1):
        M[0][j] = j * delta
    for i in range(1, n + 1):
        # charX = X[i - 1][1]
        for j in range(1, m + 1):
            # charY = Y[j - 1][1]

            M[i][j] = min(
                alpha + M[i - 1][j - 1],
                delta + M[i - 1][j],
                delta + M[i][j - 1],
            )
    print(M)
    return M[n][m]


X = [("P", 14), ("A", 1), ("L", 10), ("E", 5), ("T", 18), ("T", 18), ("E", 5)]
Y = [("P", 14), ("A", 1), ("L", 10), ("A", 1), ("T", 18), ("E", 5)]
delta = 2
m = len(Y)
n = len(X)
print("Scegli l'alpha [1 = alpha costante][2 = alpha matrice]: ")
x = input()
if x == "1":
    alpha = 1
    print(f"Soluzione ottima :\n {SeqAlAlpha1(m, n, X, Y, delta, alpha)}")
elif x == "2":
    alpha = np.zeros((21, 21), dtype=int)
    for i in range(21):
        for j in range(21):
            if i == j:
                alpha[i][j] = 0
            else:
                alpha[i][j] = np.random.randint(1, 300)
    print(f"Matrice alpha :\n {alpha}")
    print(f"Soluzione ottima :\n {SeqAl(m, n, X, Y, delta, alpha)}")
else:
    print(Fore.RED + "Errore nell'input")
    exit()
print(Style.RESET_ALL)

print(
    "Osservazione :\n- Se alpha = 1 (Assunzione) allora ottengo il caso in cui il costo è arbitrariamente piccolo (O(n)+O(m))\n- Se alpha = matrice dei valori (vedi slide) allora il costo sarà diverso (possibile arbitrariamente grande)"
)
