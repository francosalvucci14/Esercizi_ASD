# a = [1,3,2,4]
# b = [6,4,5,3]

a = [1,4,6,7,5,7,9,2,7]
b = [6,4,8,5,1,2,3,5,7]
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
            return cx
        if k < a[cx]:
            rx = cx-1
        else: # k > a[cx]
            lx = cx+1
    return -1

def jaccard(a,b):
    n_a = len(a)
    n_b = len(b)
    merge_sort(a,0,n_a)
    merge_sort(b,0,n_b)
    print(a,b)
    inter = 0
    for i in range(n_a):
        el_b = bin_search(b,a[i])
        if el_b == -1:
            el_b=0
        else:
            inter+=1
        if i < n_a-1:
            if a[i] == a[i+1]:
                inter-=1
            #print(list_b[el_b])
    #print(inter)
    #print(a&b)
    # for i in range(n_b):
    #     el_a = bin_search(a,b[i])
    #     if el_a == -1:
    #         el_a=0
    #     else:
    #         inter+=1
    #     if i < n_b-1:
    #         if b[i] == b[i+1]:
    #             inter-=1
    
    union = n_a+n_b-inter #Principio di inclusione-esclusione
    #print(union)
    print(inter,union)
    jaccard = inter/union
    print(jaccard)

jaccard(a,b)
