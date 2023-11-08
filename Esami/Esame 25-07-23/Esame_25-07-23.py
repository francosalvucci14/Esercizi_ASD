
def kpicco(a):
    n=len(a)
    if n == 1 or n == 2:
        return 0
    k=0
    max_k=0

    for i in range(1,n-1):
        if a[i]>a[i+1] and a[i]>a[i-1]:
            k+=1
            max_k+=k

        else:
            k=0
    return max_k

def TrovaKPicco(A):
    n = len(A)
    max_k = 0
    current_k = 0
    pos = 0
    for i in range(1, n - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            current_k += 1
            max_k += max(max_k, current_k)
            pos = i
        else:
            current_k = 0

    return max_k,pos

# def picco(A):
#     n = len(A)
#     crescente = True
#     decres = True
#     i=1
#     k=0
#     picco = 0
#     while crescente:
#         crescente = False
#         if A[i] < A[i+1]:
#             crescente = True
#             i+=1
#         else:
#             crescente = False
#             #picco = i
#     j=i
#     while decres:
#         decres = False
#         if A[j]<A[j-1]:
#             decres = True
#             j-=1
#         else:
#             decres = False
#     picco = j
#     for i in range(picco):

#     return k
    
#A = [2,3,4,5,6,3,2,8]
A = [5,2,8,3,1,0]
result,pos = TrovaKPicco(A)
print("Il valore massimo di k-picco nel vettore A è:", result, "in posizione:",pos)

print(kpicco(A))

