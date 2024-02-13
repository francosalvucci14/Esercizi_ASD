def bin_search(a,k):
    n = len(a)
    #eseguo binsearch per b
    lx, rx = 0, n-1
    while lx <= rx: # fintanto che lo spazio di ricerca non è vuoto
        cx = (lx + rx)//2
        if k >= a[cx] and ( cx == n-1 or a[cx+1] > k ):
            return cx+1
        if k < a[cx]:
            rx = cx-1
        else: # k > a[cx]
            lx = cx+1
    return 0
        
def merge( a, lx, cx, rx ):
    '''
    Precondizione: a lista e a[lx:cx] e a[cx:rx] ordinate in modo non decrescente
    Modifica a fondendo le due sottoliste in modo che a[lx:rx] risulti ordinata
    
    Sia n = len(a), e k = rx-lx
    
    Costo: lineare in k
    '''
    i, j = lx, cx # indice in a[lx:cx] ed in a[cx:rx] rispettivamente
    c = [] # lista di output
    
    # Costo O(k) 
    while i < cx and j < rx:
        if a[i] < a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1
    
    # Costo O(k)
    c += a[i:cx] + a[j:rx]
    
    #a = a[:lx] + c + a[rx:] Costo lx + (rx-lx) + (n-rx) = O(n)

    # Costo O(k)
    for i in range(len(c)):
        a[lx+i] = c[i]
def merge_sort(a, lx, rx):
    '''
    Precondizione: a una lista numerica
    Ordina a[lx:rx]
    '''
    
    if lx <= rx-2: # almeno due elementi in a[lx:rx]
        cx = (rx+lx)//2
        merge_sort(a, lx, cx)
        merge_sort(a, cx, rx)
        a = merge(a, lx, cx, rx)

def Alg(a):
    n=len(a)
    merge_sort(a,0,n)
    print(a)
    for i in a:
        j = bin_search(a,i**2)
        if j != -1:
            return True

a = [10,1,6,3,4,0,8,2]
print(Alg(a))
