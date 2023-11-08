a = [1,4,3,2,5,7]
def bin_search( a, k ):
    n = len(a)
    lx, rx = 0, n-1
    while lx <= rx:
        cx = (lx + rx)//2
        print(f"cx : {cx}")
        if a[cx]>=k:
            return cx
        else:
            lx = cx+1
    return -1
def creaoracolo(a,k):
    y=[0]*k
    n=len(a)
    for i in range(n-1):
        y[a[i]]+=1
    print(f"Array Y: {y}")
    for i in range(1,k):
        y[i]=y[i]+y[i-1]
    return y
def query(a,x):
    n=len(a)
    j = bin_search(a,x)
    print(j)
    if j == -1:
        return n+1
    else:
        return j

a_o = creaoracolo(a,7)
print(f"Oracolo : {a_o}")
print(query(a_o,1))