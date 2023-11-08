a = [1,2,3,4,5,6,7]
b = [2,13,8,10,6,4,11]

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

def Algoritmo(a,b,x):
    merge_sort(a,0,len(a))
    merge_sort(b,0,len(b))

    min = x-(a[0]+b[0])
    for i in range(len(a)):
        n2 = bin_search(b,x-a[i])
        if x-(a[i]+n2) == 0:
            min = 0
            ind = i
            ind2 = n2
        elif x-(a[i]+n2)<min:
            min = x-(a[i]+n2)
            ind = i
            ind2 = n2
    i = ind
    j = bin_search(b,ind2)
    return (i,j)

print(Algoritmo(a,b,9))