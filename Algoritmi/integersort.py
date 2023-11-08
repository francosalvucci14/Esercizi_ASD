def IntegerSort(A,k):
    Y=[0]*k
    n=len(A)
    for i in range(n-1):
        Y[A[i]]+=1
    j=0
    for i in range(k):
        while(Y[i]>0):
            A[j]=i
            j+=1
            Y[i]-=1
    return A

#a = [1,10,4,3,3,5,20]
a = [5,0,12,55,100]

max_el = max(a)
print(IntegerSort(a,max_el))
