def QuickSort(A,i,f):
    if(i<f):
        m=Partition(A,i,f)
        QuickSort(A,i,m-1)
        QuickSort(A,m+1,f)
    return A
def Partition(A,i,f):
    x=A[i]
    inf=i
    sup=f+1
    while True:
        inf=inf+1
        while inf<= f and A[inf]<= x:
            inf=inf+1
        sup=sup-1
        while A[sup]>x:
            sup=sup-1
        if inf< sup:
            A[inf],A[sup]=A[sup],A[inf]
        else:
            break
    A[i],A[sup]=A[sup],A[i]
    return sup

a = [1,10,4,3,3,5,20]

print(QuickSort(a,0,len(a)-1))