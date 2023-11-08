a = [5, 4, 6, 8]
b = [(1, "R"), (3, "B"), (4, "R"), (5, "B")]
# b = [1,3,4,5]


def bin_search(a, k):

    n = len(a)
    lx, rx = 0, n-1
    somma = 0
    while lx <= rx:  # fintanto che lo spazio di ricerca non è vuoto
        cx = (lx + rx)//2
        if k > a[cx][0]:
            somma += 1
            lx = cx+1
        else:
            rx = cx-1
        # else: # k > a[cx]
        #     lx = cx+1
    return somma


def algoritmo(a, b, k):
    n = len(a)
    sol = 0
    X = []*n
    for i in range(n):
        if b[i][1] == "R":
            X.append(b[i])
    print(X)
    # in questo caso il vettore b è ordinato, in caso contrario basta ordina b tramite il buketsort, costo n+k
    for i in range(n):
        num_el_b = bin_search(X, a[i])
        if num_el_b >= k:
            sol += 1
    return sol


sol = algoritmo(a, b, 3)
print(sol)
