a = [1,2,3,3,4,6]
b = [2,3,4,4,7,8]

def bin_search( a, k ):
    n = len(a)
    lx, rx = 0, n-1
    list_dict = list(a)
    while lx <= rx: # fintanto che lo spazio di ricerca non è vuoto
        cx = (lx + rx)//2
        if k == list_dict[cx]:
            return cx
        if k < list_dict[cx]:
            rx = cx-1
        else: # k > a[cx]
            lx = cx+1
    return -1

def algoritmo(a,b):
    n=len(a)-1
    y=[0]*max(b)
    for i in range(n):
        y[b[i]]+=1
    c=0
    for i in range(n):
        c+=y[a[i]]
    return c

def alg2(a,b):
    #creo un dict basato su b, dove ogni coppia chiave valore corrisponde al valore dell'elemento i
    #e al numero di occorrenze 
    #poi applico il binary search su b, per ogni elemento di a, e se l'elemento esiste nel dict allora il contatore
    # degli accoppiamenti sarà incrementato in base al valore del num di accoppiamenti
    n=len(a)
    acc=0
    dict_b={}
    print(a)
    print(b)
    for i in b:
        if i in dict_b:
            dict_b[i]+=1
        else:
            dict_b[i]=1
    print(dict_b)
    for i in a:
        j=bin_search(dict_b,i)
        if j!=-1:
            acc+=dict_b[i]
        
    return acc
print(algoritmo(a,b))