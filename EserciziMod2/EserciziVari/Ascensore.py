def Ascensore(p: list, C: int) -> int:
    n = len(p)

    OPT = [[0] * C for _ in range(n)]

    for c in range(C):
        if c >= p[0]:
            OPT[0][c] = 1
        else:
            OPT[0][c] = 0

    for i in range(n):
        for c in range(C):
            if c >= p[i]:
                OPT[i][c] = max(OPT[i - 1][c], OPT[i - 1][c - p[i]] + 1)
            else:
                OPT[i][c] = OPT[i - 1][c]
    return OPT[n - 1][C - 1]


p = [
    10,
    5,
    15,
    10,
]
C = 25
print(Ascensore(p, C))
