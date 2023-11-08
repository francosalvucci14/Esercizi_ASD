def CreaOracolo(x,a,b):
    n = len(x)
    merge_sort(x,0,n)
    print(x)
    if b>x[n-1]:
        return (n-bin_searchTOT(x,a,0))
    if a<x[0]:
        return bin_searchTOT(x,b,1)
    if b<a:
        return -1
    m_b = bin_searchTOT(x,b,1)
    m_a = bin_searchTOT(x,a,0)
    #print(f"elementi <= di b = {b}:{m_b}, elementi < di a = {a}:{m_a}")
    tot = m_b-m_a
    #print(f"elementi compresi tra a e b {tot}")
    return tot
def bin_searchTOT(a,k,flag):
    '''per scegliere se eseguire il binsearch per a o per b si utilizza il flag
    flag = 0 per a, flag = 1 per b
    '''
    n = len(a)
    if flag == 0:
        #eseguo binsearch per a
        left = 0
        right = n - 1
        count = 0
        while (left <= right):
            cx = int((right + left) / 2)
            # Check if cxdle element is
            # less than or equal to key
            if (a[cx] < k):
                # At least (cx + 1) elements are there
                # whose values are less than
                # or equal to key
                count = cx + 1
                left = cx + 1
            # If key is smaller, ignore right half
            else:
                right = cx - 1
        return count
    else:
        #eseguo binsearch per b
        lx, rx = 0, n-1
        while lx <= rx: # fintanto che lo spazio di ricerca non è vuoto
            cx = (lx + rx)//2
            if k >= a[cx] and ( cx == n-1 or a[cx+1] > k ):
                return cx+1
            if k < a[cx]:
                rx = cx-1
            else: # k > a[cx]
                lx = cx+1
        return 0
"""def binSearchLT(a, key):
	n = len(a)
	left = 0
	right = n - 1
	count = 0
	while (left <= right):
		cx = int((right + left) / 2)
		# Check if cxdle element is
		# less than or equal to key
		if (a[cx] < key):
			# At least (cx + 1) elements are there
			# whose values are less than
			# or equal to key
			count = cx + 1
			left = cx + 1
		# If key is smaller, ignore right half
		else:
			right = cx - 1
	return count

def binSearchGEQ( a, k ):
    n = len(a)
    lx, rx = 0, n-1
    while lx <= rx: # fintanto che lo spazio di ricerca non è vuoto
        cx = (lx + rx)//2
        if k >= a[cx] and ( cx == n-1 or a[cx+1] > k ):
            return cx+1
        if k < a[cx]:
            rx = cx-1
        else: # k > a[cx]
            lx = cx+1
    return 0
"""
def merge( a, lx, cx, rx ):
    '''
    Precondizione: a lista e a[lx:cx] e a[cx:rx] ordinate in modo non decrescente
    Modifica a fondendo le due sottoliste in modo che a[lx:rx] risulti ordinata
    
    Sia n = len(a), e k = rx-lx
    
    Costo: lineare in k
    '''
    i, j = lx, cx # indice in a[lx:cx] ed in a[cx:rx] rispettivamente
    c = [] # lista di output
    
    # Costo O(k) 
    while i < cx and j < rx:
        if a[i] < a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1
    
    # Costo O(k)
    c += a[i:cx] + a[j:rx]
    
    #a = a[:lx] + c + a[rx:] Costo lx + (rx-lx) + (n-rx) = O(n)

    # Costo O(k)
    for i in range(len(c)):
        a[lx+i] = c[i]
def merge_sort(a, lx, rx):
    '''
    Precondizione: a una lista numerica
    Ordina a[lx:rx]
    '''
    
    if lx <= rx-2: # almeno due elementi in a[lx:rx]
        cx = (rx+lx)//2
        merge_sort(a, lx, cx)
        merge_sort(a, cx, rx)
        a = merge(a, lx, cx, rx)

#a = [2,1,10,5,7,0,4,9,6,8,11,1,2]
x = [1,-10,4.3,3.35,3,-5,20,-5,-5]
n = len(x)
#caso [a,b]
a = -5
b = 4.6
#caso (a,b]
'''a = -n**100
b = 15'''
#caso [a,b)
'''a = -5
b = n**100'''
print(f"Numero di elementi tra {a} e {b} : {CreaOracolo(x,a,b)}")

