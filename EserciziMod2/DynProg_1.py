def FindOPT(A):
    n = len(a)
    OPT = [0] * n
    OPT[0] = A[0][1]
    OPT[1] = max(A[0][1], A[1][1])

    for i in range(2, n):
        OPT[i] = max(OPT[i - 1], A[i][1] + OPT[i - 2])
    print(OPT)
    return OPT[n-1],OPT

def FindSol(O,A):
    n = len(O)
    S = []
    j=n-1
    while j>=2:
        if O[j-1]>=O[j-2]+A[j][1]:
            j-=1
        else:
            S.append(A[j][0])
            j-=2
    if (j == 1) and (A[1][1]>A[0][1]):
        S.append(A[1][0])
    else:
        S.append(A[0][0])
    return S
    
a = [(1, 1), (2, 4), (3, 8), (4, 4), (5, 3), (6, 10)]
#a = [(1, 1), (2, 4), (3, 5), (4, 4)]
print(f"Istanza : {a}")
SolOtt,OPT = FindOPT(a)
Soluzione = FindSol(OPT,a)

print(f"Soluzione Ottima : {SolOtt}")
print(f"Soluzione effettiva (Posizione dei nodi) : {Soluzione}")
