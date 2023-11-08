a = [0,0,1,0,1,1,0,1]
#a = [0,0,1,0,1,1,1,0]

def Algoritmo(a):
    n=len(a)
    Z = [0]*n
    U = [0]*n
    
    if a[0]==0:
        Z[0] = 1
    else:
        U[0] = 1
    
    for j in range(1,n):
        if a[j] == 0:
            Z[j] = Z[j-1]+1
        else:
            Z[j] = Z[j-1]
    
    U[n-1] = 0
    
    for j in range(n-2,-1,-1):
        U[j] = U[j+1]+a[j+1]
    
    for i in range(n):
        if Z[i] == U[i]:
            return i+1
    return 0

# Versione equivalente

def Taglia(a):
    count = 0
    for i in range(len(a)):
        count=count+a[i]
    return count

print(Algoritmo(a))
print(Taglia(a))