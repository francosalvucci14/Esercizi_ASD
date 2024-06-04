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

def max_battery_level(M,delta):
    n = len(M)
    m = len(M[0])

    # Creazione di una matrice dp per memorizzare i massimi livelli di batteria
    OPT = [[0] * (m) for _ in range(n)]

    OPT[0][0] = delta

    for i in range(1,n):
        for j in range(1,m):
            if M[i][j] > delta:
                OPT[i][j] = delta + max(OPT[i - 1][j], OPT[i][j - 1])-1
            else:
                OPT[i][j] = M[i][j] + max(OPT[i - 1][j], OPT[i][j - 1])-1
    printMatrix(OPT)
    return OPT[n - 1][m - 1]

M = [
    [0, 3, 2, 6], 
    [7, 5, 4, 9], 
    [3, 10, 6, 3], 
    [2, 7, 10, 4]
]

delta = 5 
result = max_battery_level(M,delta)
print(result)

