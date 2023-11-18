def InsertionSort(a):
    n=len(a)
    #print(len(a))
    for k in range(n-1):
        x = a[k+1]
        j=k
        while j>0 and a[j]>x:
            a[j+1] = a[j]
            j=j-1
        a[j]=x
    return a 

a = [8,4,6,3,1,1,5,2,4,8,6,2,0,4,7,9]
a_s = InsertionSort(a)
print(len(a_s))
print(a_s)
