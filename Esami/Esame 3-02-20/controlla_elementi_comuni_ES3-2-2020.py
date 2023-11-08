"""Siano dati due vettori A[1 : n] e B[1 : n] di n numeri. Si fornisca un algoritmo con complessit`a O(n log n)
che verifiche se A e B hanno almeno un elemento in comune, ovvero se esistono due indici i e j tali che
A[i] = B[j]. Si fornisca lo pseudocodice dell'algoritmo."""

def merge( a, lx, cx, rx ):
    i, j = lx, cx # indice in a[lx:cx] ed in a[cx:rx] rispettivamente
    c = [] # lista di output
    while i < cx and j < rx:
        if a[i] < a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1

    c += a[i:cx] + a[j:rx]

    for i in range(len(c)):
        a[lx+i] = c[i]

def merge_sort(a, lx, rx):

    if lx <= rx-2: # almeno due elementi in a[lx:rx]
        cx = (rx+lx)//2
        merge_sort(a, lx, cx)
        merge_sort(a, cx, rx)
        a = merge(a, lx, cx, rx)

def controlla(a,b):
    n=len(a)
    merge_sort(a,0,n)#costo nlogn
    merge_sort(b,0,n)#costo nlogn
    print(a,b)
    trovato=False
    i,j=0,0
    #intero while costo logn,eseguito n volte
    while (i<=n) and (j<=n) and not trovato:
        if a[i]<b[j]:
            i+=1
        elif a[i]>b[j]:
            j+=1
        else:
            trovato=True
    if trovato:
        print(f"Indici ({i},{j})")
    else:
        print("Niente da fare")
    #totale O(nlogn+nlogn)=O(nlogn)
a = [2,10,7,0,4,9,6,8,11,1,2,3]
b = [27,12,84,7,10,14,9,5,58,11,11,22]

controlla(a,b)