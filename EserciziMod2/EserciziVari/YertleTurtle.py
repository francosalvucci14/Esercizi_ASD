def Turtle(p: list, r: list, i: int, j: int, OPT: dict = dict()) -> int:
    """
    OPT[i][j] = numero massimo di tartarughe, il cui peso complessivo è <= j
    """
    n = len(p)
    if (i, j) in OPT:
        return OPT[i, j]
    if i == n - 1 and p[i] <= j:
        OPT[i, j] = 1
    elif i == n - 1 and p[i] > j:
        OPT[i, j] = 0
    elif p[i] > j:
        OPT[i, j] = Turtle(p, r, i + 1, j, OPT)
    else:
        OPT[i, j] = max(
            Turtle(p, r, i + 1, j, OPT), Turtle(r, p, i + 1, min(j - p[0], r[0]), OPT)
        )
    print(OPT)
    return OPT[i, j]


pesi = [1000, 10000, 10000000, 5]
resistenze = [20, 4, 1, 150421354]
maxr = max(resistenze)

cache = dict()
ris = Turtle(pesi, resistenze, 0, maxr, cache)
print(ris)
