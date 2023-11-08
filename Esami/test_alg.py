def algoritmo(v,h):
    n=len(v)
    a = [0]*(n+1)
    if v[0] == "B":
        a[0]=0
    else:
        a[0] = h+1
    for i in range(1,n):
        if v[i] == "N":
            a[i]=h+1
        else:
            a[i]=max(a[i-1]-1,0)
    b = [0]*(n+1)
    if v[n-1] == "B":
        b[n]=0
    else:
        b[n-1]=h+1
    for i in range(n-1,0,-1):
        if v[i] == "N":
            b[i]=h+1
        else:
            b[i]=max(b[i+1]-1,0)
    count=0
    for i in range(n):
        if a[i]>0 and b[i]>0:
            count+=1
    print(a,b)
    return count

v = ["B", "N", "N", "B", "B", "N", "B", "N", "B", "B"]
print(algoritmo(v,2))