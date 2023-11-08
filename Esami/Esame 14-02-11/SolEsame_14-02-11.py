a = [0,1,0,1,1,1,0,1,1]

def Algoritmo(a):
    n=len(a)
    x=[0]*n
    y=[0]*n
    #costruisco X
    if a[0] == 1:
        x[0]+=1
    for i in range(1,n):
        
        x[i] = x[i-1]+a[i]
    print(x)
    # costruisco Y
    if a[n-1] == 0:
        y[n-1]+=1
    for i in range(n-2,-1,-1):
        
        y[i] = y[i+1]+a[i-1]
        
    print(y)
    # ritorno l'indice
    for i in range(n):
        if x[i] == y[i]:
            return i
    return -1

def Algoritmo2(a):
    n=len(a)
    if a[n-1] == 1:
        return -1
    if a[n-1] == 0:
        return n
    AlgRic(a,0,n)

def AlgRic(a,i,f):
    if i > f:
        return -1
    m = (i+f)//2
    if a[m] == 0:
        if a[m+1] == 1:
            return m
        else:
            return AlgRic(a,m+1,f)
    if a[m] == 1:
        if a[m-1] == 0:
            return m-1
        else:
            return AlgRic(a,i,m-1)   

print(Algoritmo(a))
b = sorted(a)
print(AlgRic(b,0,len(b)-1))