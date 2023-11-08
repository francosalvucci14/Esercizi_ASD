a = [1,2,3,4]
b = [8,1,5,4]


def alg2(a, b):
    n = len(a)
    
    x = [0]*n
    y = [0]*n
    
    x[0] = a[0]

    b2 = b[::-1]
    y[0] = b2[0]

    for i in range(1, n):
        x[i] = x[i-1] + a[i]
        y[i] = y[i-1] + b2[i]
    
    c = 0
    for j in range(n):
        if x[j] < y[j]:
            c += 1
    return c

def alg(a,b,mid):
    n=len(a)
    
    sum_A,sum_B = 0,0
    for i in range(mid+1):
        sum_A += a[i]
    for j in range(mid+1,n):
        sum_B += b[j]
    if sum_A > sum_B:
        return mid+1
    elif sum_A < sum_B:
        return alg(a,b,mid+1)
    else:
        return alg(a,b,mid-1)

def alg3(a,b):
    n=len(a)
    lx,rx = 0,n-1
    sum_A,sum_B = 0,0
    while lx <= rx:
        mid = (rx+lx)//2
        for i in range(mid+1):
            sum_A += a[i]
        for j in range(mid+1,n):
            sum_B += b[j]
        if sum_A > sum_B:
            return mid+1
        elif sum_A < sum_B:
            lx = mid+1
        else:
            rx = mid-1

print(alg2(a, b))
rx,lx = 0,len(a)-1
mid = (rx+lx)//2
print(alg(a, b,mid))
print(alg3(a,b))
