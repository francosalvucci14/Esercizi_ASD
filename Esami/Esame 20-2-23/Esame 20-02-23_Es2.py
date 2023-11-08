#a = [0, 1, 0, 1]
#a = [0,1,0,0,1,1,0]
a = [0,0,0,1]

def algoritmo(a, k):
    n = len(a)
    b = CreaOracolo(a)
    j = q(b, k)
    if j < 0:
        return -1
    else:
        return j

def CreaOracolo(a):
    n = len(a)
    print(a)
    b = [0]*n
    for i in range(n-1, -1, -1):
        if a[i] == 1:
            b[i] == 0
        else:
            b[i] += 1
    print(b)
    return b

def q(a, i):
    return i+a[i]

def CreaOracolo2(a):
    n=len(a)
    b=[0]*n
    for i in range(1,n):
        b[i] = b[i-1]+a[i]
    print(b)
    return b
print(algoritmo(a, 1))
