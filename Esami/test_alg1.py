import math
a = [3,6,10,13,21]
b = [19,14,9,5,2]
n=5
delta = 8
def algoritmo(a,b,n,delta):
    m = math.floor(n/2)
    if (abs(a[m]-b[m])) > delta:
        return 
    return ricbin_s(a,b,0,m,delta),ricbin_d(a,b,m+1,n,delta)
def ricbin_s(a,b,i,j,delta):
    m = math.floor((i+j)/2)
    if (i==j) and (abs(a[m]-b[m])==delta):
        return m
    if i<j:
        if (abs(a[m]-b[m]))>delta:
            ricbin_s(a,b,m+1,j,delta)
        else:
            ricbin_s(a,b,i,m,delta)
        if (abs(a[i]-b[i]))<=delta:
            return i
        else:
            return j
        
def ricbin_d(a,b,i,j,delta):
    m = math.floor((i+j)/2)
    if (i==j) and (abs(a[m]-b[m])==delta):
        return m
    if i<j:
        if (abs(a[m]-b[m]))>delta:
            ricbin_d(a,b,i,m,delta)
        else:
            ricbin_d(a,b,m+1,j,delta) 
        if (abs(a[i]-b[i]))<=delta:
            return i+1
        else:
            return j-1
          
print(algoritmo(a,b,n,delta))