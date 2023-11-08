a = [(-2,"R"),(5,"N"),(9,"R"),(11,"N")]

def algoritmo(a):
    orc = oracolo(a)
    valore_spec = Interroga(orc,-2)
    return valore_spec
def oracolo(a):
    n=len(a)
    speciale = False
    primo_rosso = None
    ultimo_rosso = None
    oracolo=[(0,0)]*n

    for i in range(n):
        if a[i][1] == "R" and primo_rosso==None:
            primo_rosso = a[i][0]
        if a[i][1] == "R" or ((a[i][0]+ultimo_rosso)%2==0):            
            ultimo_rosso = a[i][0]
            speciale = True
        else:
            speciale = False
        oracolo[i] = (a[i][0],speciale)

    return oracolo
def bin_search( a, k ):
    n = len(a)
    lx, rx = 0, n-1
    while lx <= rx: # fintanto che lo spazio di ricerca non è vuoto
        cx = (lx + rx)//2
        if k == a[cx][0]:
            return cx
        if k < a[cx][0]:
            rx = cx-1
        else: # k > a[cx]
            lx = cx+1
    return -1
def Interroga(a,x):
    speciale = bin_search(a,x)
    if speciale == -1:
        return False
    if speciale != -1 and a[speciale][1] == True:
        return True,speciale
    else:
        return False

print(algoritmo(a))
