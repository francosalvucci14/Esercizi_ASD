def Punteggio(p: list, t: list, T: int) -> int:
    """
    OPT[i][j] = punteggio massimo ottenibile rispondendo correttamente alle domande da 1 a i, in tempo j (j=1,...,T)
    """
    n = len(p)
    OPT = [[0] * T for _ in range(n)]
    # print(OPT)
    for j in range(T):
        if j >= t[0]:
            OPT[0][j] = p[0]
        else:
            OPT[0][j] = 0

    for i in range(1, n):
        for j in range(T):
            if j >= t[i] and (OPT[i - 1][j] < OPT[i - 1][j - t[i]] + p[i]):
                OPT[i][j] = OPT[i - 1][j - t[i]] + p[i]
            else:
                OPT[i][j] = OPT[i - 1][j]
    #    print(OPT)
    return OPT[n - 1][T - 1]


p = [5, 10, 2, 3]
t = [5, 24, 10, 26]
T = 25
__import__("pprint").pprint(Punteggio(p, t, T))
