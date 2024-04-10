import numpy as np

def Knapsack(n,W,pesi,valori):
    M=np.zeros((n,W+1),dtype=int)
    print(f"Matrice Iniziale : \n{M}\n")
    for w in range(W+1):
        M[0][w]=0

    for i in range(n):
        for w in range(W+1):
            if pesi[i]>w:
                M[i,w]=M[i-1,w]
            else:
                M[i,w] = max(M[i-1,w],valori[i]+M[i-1,w-pesi[i]])
    print(f"Matrice Finale dei valori : \n{M}\n")
    return M[n-1,W]

W=11
pesi=[1,2,5,6,7]
valori=[1,6,18,22,28]
n=len(pesi)
print(f"Istanza : \nPesi : {pesi}\nValori : {valori}")
print(f"Soluzione ottima al problema : {Knapsack(n,W,pesi,valori)}")

