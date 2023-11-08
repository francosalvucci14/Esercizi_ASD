def algoritmo(a,b):
    n_a = len(a)
    n_b = len(b)
    merge_sort(a,0,n_a)
    merge_sort(b,0,n_b)
    print(a,b)
    for i in range(n_a):
        j = bin_search(b,a[i])
        if j != -1:
            return i+1,j
    if j == -1:
        print("non ci sono elementi")
def bin_search( a, k ):
    n = len(a)
    lx, rx = 0, n-1
    while lx <= rx: # fintanto che lo spazio di ricerca non è vuoto
        cx = (lx + rx)//2
        if k == a[cx]:
            return cx+1
        if k < a[cx]:
            rx = cx-1
        else: # k > a[cx]
            lx = cx+1
    return -1
def merge( a, lx, cx, rx ):
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
    for i in range(len(c)):
        a[lx+i] = c[i]
def merge_sort(a, lx, rx):

    
    if lx <= rx-2: # almeno due elementi in a[lx:rx]
        cx = (rx+lx)//2
        merge_sort(a, lx, cx)
        merge_sort(a, cx, rx)
        a = merge(a, lx, cx, rx)

a = [1,4,9,5]
b = [2,6,3,10]

print(algoritmo(a,b))