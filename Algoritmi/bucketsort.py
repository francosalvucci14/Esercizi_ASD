def BucketSort(x,k):
    arr = []
    for i in range(k):
        arr.append([])
          
    # Put array elements in different buckets 
    for j in x:
        index_b = int(k * j) 
        arr[index_b-1].append(j)
      
    # Sort individual buckets 
    for i in range(k):
        arr[i] = sorted(arr[i])
          
    # concatenate the result
    y=0
    for i in range(k):
        for j in range(len(arr[i])):
            x[y] = arr[i][j]
            y += 1
    return x

a = [1,10,4,3,3,5,20]
print(BucketSort(a,max(a)))

#da vedere
