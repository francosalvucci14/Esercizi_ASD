"""
Esercizio Pista ciclabile con ripetitori
Input : Costi per i ripetitori Low
        Costi per i ripetitori High
"""


def esercizio(l, h):
    n = len(l)
    opt = [0] * (n + 3)

    for i in range(n - 1, -1, -1):
        opt[i] = min(l[i] + opt[i + 1], l[i] + opt[i + 2], h[i] + opt[i + 3])
        # if (l[i]+opt[i+1] or l[i]+opt[i+2]) == opt[i]:
        #     print(f"LOW in posizione {i+1}")
        # else:
        #     print(f"HIGH in posizione {i+1}")
    return opt[0], opt


def ricostruzione(opt, l, h):
    n = len(l)
    i = 0
    soluzione = [""] * n
    soluzione[n - 1] = "L"
    if l[0] < h[0]:
        soluzione[0] = "L"
    else:
        soluzione[0] = "H"
    for i in range(1, n):

        if soluzione[i - 1] == "L":
            if (l[i] + l[i + 1]) < h[0]:
                soluzione[i] = "L"
            else:
                soluzione[i] = ""
        if soluzione[i - 1] == "":
            if i + 1 > n - 1 or i + 2 > n - 1:
                break
            if (l[i] + l[i + 1] + l[i + 2]) > h[i]:
                soluzione[i] = "H"
            else:
                soluzione[i] = "L"
        if soluzione[i - 1] == "H":
            soluzione[i] = ""
            soluzione[i + 1] = ""
    return soluzione


l = [2, 1, 3, 4, 4, 7, 1]
h = [5, 8, 3, 5, 4, 8, 5]

sol_ottima, opt = esercizio(l, h)
print(sol_ottima)
print(opt)
print(ricostruzione(opt, l, h))
