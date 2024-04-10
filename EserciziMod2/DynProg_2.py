from colorama import Fore, Back, Style

def Algoritmo(r,b,g):
    n=len(r)
    red=[0]*n
    blue=[0]*n
    green=[0]*n

    red[0]=r[0]
    blue[0]=b[0]
    green[0]=g[0]
    for i in range(1,n):
        red[i] = r[i]+min(blue[i-1],green[i-1])
        blue[i] = b[i]+min(red[i-1],green[i-1])
        green[i] = g[i]+min(red[i-1],blue[i-1])
    return red,blue,green

def Ricostruzione(red,blue,green):
    min_prec = min(red[0],blue[0],green[0])
    if min_prec == red[0]:
        print("Casa 1 colorata di"+Fore.RED+" rosso")
    elif min_prec == blue[0]:
        print("Casa 1 colorata di"+Fore.BLUE+" blue")
    else:
        print("Casa 1 colorata di"+Fore.GREEN+" verde")
    n=len(red)
    for i in range(1,n):
        min_attuale = min(red[i],blue[i],green[i])
        if min_attuale == red[i] and min_prec == red[i-1]:
            min_attuale = min(blue[i],green[i])
        if min_attuale == blue[i] and min_prec == blue[i-1]:
            min_attuale = min(red[i],green[i])
        if min_attuale == green[i] and min_prec == green[i-1]:
            min_attuale = min(red[i],blue[i])
        print(Style.RESET_ALL)
        
        if min_attuale == red[i]:
            print(f"Casa {i+1} colorata di"+Fore.RED+" rosso")
        elif min_attuale == blue[i]:
            print(f"Casa {i+1} colorata di"+Fore.BLUE+" blue")
        else:
            print(f"Casa {i+1} colorata di"+Fore.GREEN+" verde")
        min_prec = min_attuale

r = [7,6,7,8,9,20]
g = [3,8,9,22,12,8]
b = [16,10,4,2,5,7]

n=len(r)-1
print(f'Istanza del problema (matrice dei colori in input):\nRossi:\t{r}\nVerdi:\t{g}\nBlu:\t{b}')
red,blue,green=Algoritmo(r,b,g)
print(f"\nSoluzione ottima : {min(red[n],blue[n],green[n])}")
Ricostruzione(red,blue,green)