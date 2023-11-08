import math
import numpy as np

def fibonacci6(n):
    A = [[1,1],[1,0]]
    M = potenzaDiMatrice(A,n-1)
    return M[0][0]

def potenzaDiMatrice(A,k):
    if k==0:
        return [[1,0],[0,1]]
    else:
        M = potenzaDiMatrice(A,math.floor(k/2))
        M = np.dot(M,M)
    if k%2!=0:
        M=np.dot(M,A)
    return M

print(fibonacci6(542358641248))