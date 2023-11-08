"""
Progettare un algoritmo che dato un array A[1:n], ordinato, e un intero x,
trova (se esistono) due indici i e j, i<j, tale che A[i]+A[j] = x
"""

a = [2,5,9,14,20,21,25,40]

def bin_search( a, k ):
    n = len(a)
    lx, rx = 0, n-1
    while lx <= rx: # fintanto che lo spazio di ricerca non è vuoto
        cx = (lx + rx)//2
        if k == a[cx]:
            return cx
        if k < a[cx]:
            rx = cx-1
        else: # k > a[cx]
            lx = cx+1
    return -1

def algoritmo(A,x):
    n=len(a)
    for i in range(n):
        j = bin_search(A,x-A[i])
        if A[i]+A[j] == x:
            return f"Gli indici sono : {i,j}\ne corrispondono ai seguenti valori : {A[i],A[j]}"

def algoritmo2(A,x):
    n=len(a)
    i=0
    j=n-1
    while i<j:
        if A[i]+A[j] == x:
            return (i,j)
        if A[i]+A[j]<x:
            i+=1
        else:
            j-=1
    return (-1,-1)

print(algoritmo(a,26))
print(algoritmo2(a,26))