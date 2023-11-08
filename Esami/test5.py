# a = [1,5,4,20,15]
# b = [9,78,7,6,2]
# k = [1,2,4,5,7]
a = [1,2,3,4,5,6,7,8,9,10]
#soluzione problem set del 2016/17 esercizio 2
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
def algoritmo(a,i,m):
    n=len(a)
    j = 0
    print(a[i],a[i]+1)
    
    j=bin_search(a,a[i]+1)
    if j == -1:
        m = a[i]+1
        return m
    else:
        return algoritmo(a,i+1,m)


b = algoritmo(a,0,0)
print(b)