def build_structure(A):
    n = len(A)
    prefisso_uni = [0] * (n + 1)
    prefisso_zeri = [0] * (n + 1)

    for i in range(1, n + 1):
        prefisso_uni[i] = prefisso_uni[i - 1] + A[i - 1]
        prefisso_zeri[i] = prefisso_zeri[i - 1] + (1 - A[i - 1])

    return prefisso_uni, prefisso_zeri

def query(prefisso_uni, prefisso_zeri, i, j,n):
    if i == 0:
        i=1
    if j > n:
        j=n

    num_uni = prefisso_uni[j] - prefisso_uni[i - 1]
    num_zeri = prefisso_zeri[j] - prefisso_zeri[i - 1]

    if num_uni> num_zeri:
        differenza_modulo = num_uni - num_zeri
    else:
        differenza_modulo = num_zeri - num_uni

    return differenza_modulo

# Esempio di utilizzo
vettore_A = [1, 0, 1, 1, 0, 1, 0, 0, 1]
n = len(vettore_A)
prefisso_uni, prefisso_zeri = build_structure(vettore_A)
risultato_query = query(prefisso_uni, prefisso_zeri, 0, n,n)
print(risultato_query)
