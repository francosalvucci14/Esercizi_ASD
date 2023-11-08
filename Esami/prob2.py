import math
a = [5,7,10,2,4,8,9]
def bin_search( a, k ):

    n = len(a)
    lx, rx = 0, n-1
    while lx <= rx: # fintanto che lo spazio di ricerca non è vuoto
        cx = (lx + rx)//2
        if k == a[cx]:
            return cx
        if k < a[cx]:
            rx = cx-1
        else: # k > a[cx]
            lx = cx+1
    return -1
def crea_arr_tmp(a):
	n = len(a)
	a_tmp = [0]*n
	a_tmp[0] = a[0]
	for i in range(1,n):
		a_tmp[i] = a_tmp[i-1]+a[i]
	return a_tmp
def trova_indici(a_tmp,x,i):
	j=0
	if i>len(a_tmp):
		return -1
	else:
		i2 = a_tmp[i]

	j = bin_search(a_tmp,x-a_tmp[i])
	if j>-1:
		print(a_tmp.index(i2),j)
		return (i2,j)
	else:
		trova_indici(a_tmp,x,i+1)
def soluzione(a):
	a_tmp=[]
	a_tmp = crea_arr_tmp(a)
	return trova_indici(a_tmp,40,0)
soluzione(a)