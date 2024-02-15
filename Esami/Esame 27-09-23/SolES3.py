def CreaOracolo(A):
    i=0
    c=0
    j=0
    n = len(A)
    O = [0]*n
    while i<n:
        if A[i] == 0:
            c+=1
        else:
            while j<i:
                O[j] = c
                j+=1
            c = 0
            j+=1
        i+=1
    return O
def query(O,i):
    return O[i]

a = [0,1,1,1,0,0,0,1,0,0,0,0,0,1,0]
oracolo = CreaOracolo(a)
print(oracolo)
print(query(oracolo,8))