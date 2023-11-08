#a = [1,3,5,4,2,0,11]
#a = [6, 4, 3, 2, 8, 7, 5]
#a = [1, 5, 4, 2, 3, 8]
a = [1,1,1,1]
# Soluzione esercizio

def creaoracolo(a,k):
    n = len(a)
    if n == 1:
        return 1
    b = [0]*n
    b[0] = a[0]

    for i in range(1, n):
        b[i] = b[i-1]+a[i]
    indice = InterrogaOracolo(b, k)

    return indice


def InterrogaOracolo(a, k):
    n = len(a)
    a[0] = a[0]+k
    lx, rx = 0, n-1
    print(a)
    #mid=(lx+rx)//2
    while lx < rx:
        cx = (lx+rx)//2
        # somma_primi = a[cx]-k
        # somma_parz = a[n-1]-a[cx]
        # if somma_primi >= somma_parz:
        if a[cx] < a[cx+1]:
            lx = cx+1
    return cx
    
b = creaoracolo(a,2)
print(b)
