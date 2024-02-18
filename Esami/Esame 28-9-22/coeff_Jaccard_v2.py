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
    

def Jaccar(a, b):
    n_a = len(a)
    n_b = len(b)
    i, j = 0, 0
    inter = 0
    union = 0

    # Ordino a con mergesort
    merge_sort(a,0,n_a)
    merge_sort(b,0,n_b)
    # Ordino b con mergesort
    print(a,b)

    while i < (n_a) and j < (n_b):
        if a[i] == b[j]:
            
            inter += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            
            i += 1
        else:
            
            j += 1
    union = n_a + n_b - inter
    print(inter,union)
    return inter / union


a = [0, 2, 4, 5, 5, 5]
b = [5, 4, 2, 2]

#a = [0, 4, 2, 5, 2]  # Insieme con elementi duplicati
#b = [1, 4, 2, 5, 5]  # Insieme con elementi duplicati

print(Jaccar(a,b))