def create_oracolo(A):
    n = len(A)
    Z=[0]*n
    U=[0]*n

    if A[0] == 0:
        Z[0] = 1
    else:
        Z[0] = 0
    
    for j in range(1,n):
        if A[j] == 0:
            Z[j] = Z[j-1]+1
        else:
            Z[j] = Z[j-1]
    
    U[n-1] = 0

    for i in range(n-2,-1,-1):
        U[i] = U[i+1]+A[i+1]
    
    print(Z)
    print(U)
    return Z,U


def query_difference(Z,U, i, j):
    n = len(Z)
    if i>j:
        return 0
    if j>n:
        j=n-1
    
    num_ones = U[j] - U[i-1]
    num_zeros = Z[j] - Z[i-1]
    # if num_ones < 0:
    #     num_ones = -num_ones
    # print(num_ones)
    print(num_ones)
    print(num_zeros)

    if num_zeros > num_ones:
        diff = (num_ones+num_zeros)*(-1)
    return diff


# Example Usage:
# vettore_A = [1, 0, 1, 1, 0, 1, 0, 0, 1]
vettore_A = [0, 0, 1, 0, 1, 1, 1, 0]
zeri,uni = create_oracolo(vettore_A)
result_query = query_difference(zeri,uni, 3, 6)
print(result_query)
