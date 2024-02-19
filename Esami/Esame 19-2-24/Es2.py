def Algoritmo(a):
    n=len(a)

    for i in range(1,n):
        a[i] = a[i-1]+a[i]
    
    for i in range(n):
        k=a[n-1]-a[i+1]
        if a[i]>k:
            return i

a = [5,4,3,6,7,6,2,1]
print(Algoritmo(a))