import pprint as pp
import numpy as np


def Scacchiera(n: int) -> int:
    """
    OPT[i][j] = numero di cammini possibili fino alla casella (i,j)
    """
    OPT = [[0] * n for _ in range(n)]

    for i in range(n):
        OPT[i][0] = 1
    for j in range(n):
        OPT[0][j] = 1

    for i in range(1, n):
        for j in range(1, n):
            OPT[i][j] = OPT[i - 1][j] + OPT[i][j - 1]

    return OPT[n - 1][n - 1]


def ValoreCamminoScacchiera_ConRicostruzioneCammino(score: list):
    """
    - OPT[i][j] = valore del cammino fino alla cella (i,j)
    - cammino = cammino da (0,0) a (n,n)
    """
    n = len(score[0])
    OPT = [[0] * (n + 1) for _ in range(n)]
    OPT[0][0] = score[0][0]  # caso base
    n1 = len(score)
    for i in range(1, n1):
        OPT[i][0] = OPT[i - 1][0] + score[i][0]
    for j in range(1, n):
        OPT[0][j] = OPT[0][j - 1] + score[0][j]

    for i in range(1, n):
        for j in range(1, n):
            if OPT[i - 1][j] >= OPT[i][j - 1]:
                OPT[i][j] = score[i][j] + OPT[i - 1][j]
            else:
                OPT[i][j] = score[i][j] + OPT[i][j - 1]

    # ricostruzione cammino
    cammino = [""] * (2 * n - 2)
    i = n - 1
    j = n - 1

    index = 2 * (n - 1) - 1

    for k in range(index, -1, -1):
        if OPT[i][j] == score[i][j] + OPT[i - 1][j]:
            cammino[k] = "GIU"
            i -= 1
        else:
            cammino[k] = "DESTRA"
            j -= 1

    return OPT[n - 1][n - 1], cammino


n = int(input("Scegli la dimensione della scacchiera: "))
print(f"Numero di cammini possibili in una scacchiera {n}x{n} : ", Scacchiera(n))

score = np.random.randint(1, 500, (n, n))
print("Scacchiera random:\n", score)
# score = [[3, 10, 10, 15, 6, 5, 30, 2, 1], [7, 2, 10, 1, 1, 2, 1, 3, 1000]]
OPT, cammino = ValoreCamminoScacchiera_ConRicostruzioneCammino(score)
print("Valore del cammino massimo:", OPT)
print(
    "Cammino effettivo (partendo dalla prima posizione (0,0) fino alla posizione (n,n)):\n",
    cammino,
)
