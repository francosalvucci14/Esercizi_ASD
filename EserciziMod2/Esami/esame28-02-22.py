import numpy as np


def partito(valori):
    n = len(valori)

    OPT = [0] * n

    OPT[0] = valori[0]
    for i in range(1, n):
        OPT[i] = max(valori[i] + OPT[i - 2], OPT[i - 1])
    print(OPT)
    return OPT[n - 1]


def partito_B(valori, B):
    n = len(valori)

    OPT = np.zeros((n, B + 1), dtype=int)
    for b in range(B + 1):
        OPT[0, b] = 0
    print(OPT)
    for i in range(n):
        for b in range(B + 1):
            if valori[i] + OPT[i - 2, b] < OPT[i - 1, b]:
                OPT[i, b] = OPT[i - 1, b] - 1
            else:
                OPT[i, b] = valori[i] + OPT[i - 2, b - 1]
    print(OPT)
    return OPT[n - 1][B]


# valori = [10, 2, 11, 10, 5]
valori = [1, 1, 1, 9, 10, 9, 1, 1, 8]
# valori = [9, 8, 1, 3]

print(partito(valori))
print(partito_B(valori, 3))
