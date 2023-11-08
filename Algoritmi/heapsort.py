import math

def HeapSort(a):
    heapify(a)
    heapsize = len(a)-1
    for i in range(heapsize,2,-1):
        a[0],a[i]=a[i],a[0]
        heapsize -=1
        fixHeap(1,a)
    return a

def fixHeap(i,a):
    heapsize = len(a)-1
    sx = 2*i
    dx = 2*i+1
    if sx<=heapsize and a[sx]>a[i]:
        max = sx
    else:
        max = i
    if dx<=heapsize and a[dx]>a[max]:
        max = dx
    if max != i:
        a[i],a[max] = a[max],a[i]
        fixHeap(max,a)

def heapify(a):
    heapsize = len(a)-1
    n=heapsize
    print(math.floor(n/2),int(n/2))
    for i in range(math.floor(n/2),1,-1):
        fixHeap(i,a)

a = [1,10,4,3,3,5,20]
#a = [4,1,3,2,16,9,10,14,8,7]
print(HeapSort(a))
