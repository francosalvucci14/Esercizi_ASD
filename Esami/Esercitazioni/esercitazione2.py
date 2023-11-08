a = [2,4,20,13,9,6,5,2]
#print(sorted(a,reverse=True))
b = [20,11,2,5,4,10,9,2]
def Max(a):
    n = len(a)
    if a[0]>a[1]:
        return 1
    if a[n-1]>a[n-2]:
        return n
    return MaxRic(a,1,n-2)

def MaxRic(a,i,j):
    if i>j:
        return -1
    m = (i+j)//2
    if a[m]>a[m-1] and a[m]>a[m+1]:
        return m
    if a[m]<a[m+1]:
        return MaxRic(a,m+1,j)
    else:
        return MaxRic(a,i,m-1)

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

def invert_array(A, m):
    n = len(A)
    if m >= n or m < 0:
        return A  # Non è necessario invertire nulla

    # Inverti gli elementi da m alla fine dell'array
    i = m
    j = n - 1
    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1

    return A

def Ordina(a):
    n=len(a)
    m = Max(a)
    if m != -1 and m != n:
        a_inv = invert_array(a,m)
        if m != 1:
            merge(a_inv,0,m,n)
    return a_inv

def MaxDiff(a):
    n=len(a)
    array_max = [0]*n
    array_max[n-1] = n-1
    for k in range(n-2,1,-1):
        if a[k] > a[array_max[k+1]]:
            array_max[k] = k
        else:
            array_max[k] = array_max[k+1]
    i_s = 0
    j_s = array_max[1]
    M = a[j_s]-a[i_s]
    for i in range(1,n-1):
        if (a[array_max[i+1]]-a[i])>M:
            i_s = i
            j_s = array_max[i+1]
            M = a[j_s]-a[i_s]
    return (i_s,j_s)

m = Max(a)
print(f"L'elemento massimo di A si trova in pos. {m}, che corrisponde a {a[m]}")
print(Ordina(a))
print(MaxDiff(b))
