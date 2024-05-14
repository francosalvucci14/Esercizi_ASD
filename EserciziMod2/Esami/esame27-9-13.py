import random
import pprint as pp

# Funzione aggiuntiva
def generate_matrices(n, m):
    M = []
    T = []

    for i in range(n):
        M_row = []
        T_row = []
        for j in range(m):
            val = random.randint(0, 10)  # Genera valori casuali da 0 a 9 per M
            M_row.append(val)
            if val > 0:
                T_row.append(0)  # Se M[i, j] > 0, allora T[i, j] = 0
            else:
                T_row.append(1)  # Se M[i, j] = 0, allora T[i, j] = 1
        M.append(M_row)
        T.append(T_row)

    return M, T

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

def searchPath(OPT):
    # Trova il percorso ottimo
    path = []
    i, j = n-1, m-1
    while i > 0 and j > 0:
        path.append((i, j))
        if OPT[i][j-1] + M[i][j] > OPT[i-1][j] + M[i][j]:
            j -= 1
        else:
            i -= 1
    path.append((0, 0))
    path.reverse()

    # Stampa la matrice OPT evidenziando il percorso ottimo in rosso
    for i in range(n):
        for j in range(m):
            if (i, j) in path:
                print("\033[91m{}\033[00m".format(OPT[i][j]), end="\t")
            else:
                print(OPT[i][j], end="\t")
        print()

def find_max_gold(n, m, M, T):
    # Creazione della matrice OPT
    OPT = [[0] * m for _ in range(n)]

    # Inizializzazione della prima riga e colonna
    for i in range(n):
        if T[i][0] == 1:
            OPT[i][0] = float("-inf")
        else:
            OPT[i][0] = M[i][0] + OPT[i - 1][0]

    for j in range(m):
        if T[0][j] == 1:
            OPT[0][j] = float("-inf")
        else:
            OPT[0][j] = M[0][j] + OPT[0][j - 1]

    # Calcolo dell'OPT
    for i in range(1, n):
        for j in range(1, m):
            if T[i][j] == 1:
                OPT[i][j] = float("-inf")
            else:
                OPT[i][j] = max(OPT[i][j - 1] + M[i][j], OPT[i - 1][j] + M[i][j])
    print("\nOPT:")
    #printMatrix(OPT)
    searchPath(OPT)
    # Ritorna il valore massimo nell'angolo in basso a destra di OPT
    return OPT[n - 1][m - 1]


if __name__ == "__main__":
    # n = int(input("Quante righe per le matrici?: "))
    # m = int(input("Quante colonne per le matrici?: "))
    # M, T = generate_matrices(n, m)
    n = 7
    m = 7
    M = [
        [3, 5, 0, 0, 7, 6, 2],
        [1, 10, 9, 0, 8, 4, 3],
        [3, 7, 6, 0, 0, 3, 3],
        [5, 6, 0, 4, 5, 4, 1],
        [11, 9, 8, 7, 10, 5, 4],
        [6, 0, 5, 1, 0, 9, 10],
        [7, 0, 0, 0, 0, 8, 5],
    ]
    T = [
        [0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 1, 0, 0],
    ]
    # Stampare le matrici generate
    print("Matrice M:")
    printMatrix(M)

    print("\nMatrice T:")
    printMatrix(T)

    print("\nSoluzione ottima : {}".format(find_max_gold(n, m, M, T)))
    print("Il cammino è evidenziato in \033[91mRosso\033[00m")
