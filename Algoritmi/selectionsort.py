def SelectionSort(a):
    n=len(a)
    for k in range(n-2):
        m=k+1
        for j in range(k+2,n):
            if a[j]<a[m]:
                m=j
        a[m],a[k+1]=a[k+1],a[m]
    return a
a = [0,5,6,4,7,89,2,1,6,9,78,1,32,8,47,6,21,54,8,4,5,14,89,5,5,7,96,9,8,4,1]
print(SelectionSort(a))
