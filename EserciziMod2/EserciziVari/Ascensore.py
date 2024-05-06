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


def Ascensore_memo(p: list, c: int, i: int, C: int, cache: dict = dict()) -> int:
    n = len(p)
    if (i, c) in cache:
        return cache[i, c]

    if c >= p[0]:
        cache[i, c] = 1
    else:
        cache[i, c] = 0

    if c <= C and c >= p[i]:
        cache[i, c] = max(
            Ascensore_memo(p, c, i - 1, C, cache),
            Ascensore_memo(p, c - p[i], i - 1, cache) + 1,
        )
    else:
        cache[i, c] = Ascensore_memo(p, c, i - 1, C, cache)

    return cache[i, c]


p = [
    10,
    5,
    15,
    10,
]
C = 25
print(Ascensore(p, C))
cache = dict()
n = len(p)
print(Ascensore_memo(p, 0, n, C, cache))
