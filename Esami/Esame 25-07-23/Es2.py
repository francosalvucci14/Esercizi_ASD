def kpicco(a):
    n=len(a)
    vc = [0]*n
    vd = [0]*n
    cc,cd = 0,0

    for i in range(n-1):
        if a[i]<a[i+1]:
            cc+=1
            vc[i] = cc
    for j in range(n-1,1,-1):
        if a[j]>a[j-1]:
            cd+=1
            vd[j]=cd
    
    max_picco = [0]*n
    
    for i in range(n):
        if vc[i]>vd[i]:
            max_picco[i] = vc[i]
        
        elif vc[i]<vd[i]:
            max_picco[i] = vd[i]

    max_k = max(max_picco)
    print(max_picco)
    pos = max_picco.index(max_k)
    return max_k,pos


#a = [5,2,8,3,1,0]
a = [2,3,4,5,6,3,2,8]
indice_k,posizione = kpicco(a)
print(f"Indice k di valore massimo : {indice_k}\nPosizione in cui si trova il {indice_k}-picco : {posizione}")