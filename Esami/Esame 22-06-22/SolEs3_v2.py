def Oracolo(a):
    n=len(a)

    x=[0]*n
    x[n-1] = a[n-1]
    for i in range(n-2,-1,-1):
        x[i] = x[i+1]+a[i]
    print(x)
    return x

def query(a,alpha):
    a[0] = a[0]+alpha
    n=len(a)
    i,j=0,n
    min = 0
    while i<j:
        k = (i+j)//2
        diff = a[0]-a[k]
        if diff >= a[k+1]:
            min = k
            j=k-1
        else:
            if a[k]>min:
                min = k+1
            i=k+1
    return min


a = [2,11,9,0,3,1,4]
print(a)
x = Oracolo(a)
print(query(x,2))