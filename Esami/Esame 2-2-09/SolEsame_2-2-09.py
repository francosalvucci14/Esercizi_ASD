a = [[31,10,20],
     [5,14,22],
     [8,21,22],
     [15,23,30]]

def Algoritmo(a,n,m):
    if a[0][0] > a[1][0]:
        
        for i in range(n-1):
            if a[i][0]>a[i+1][0]:
                a[i][0],a[i+1][0] = a[i+1][0],a[i][0]
            else:
                continue
        i+=1
        for j in range(m-1):
            if a[i][j]>a[i][j+1]:
                a[i][j],a[i][j+1] = a[i][j+1],a[i][j]
            else:
                continue
    
    print(a)

Algoritmo(a,4,3)