def maggioranza(V, start, end):
    # Caso base della ricorsione: se il vettore ha un solo elemento, restituisci quell'elemento
    if start == end:
        return V[start]

    # Divide il vettore in due metà
    mid = (start + end) // 2

    # Trova ricorsivamente un elemento di maggioranza nella prima metà
    x1 = maggioranza(V, start, mid)

    # Trova ricorsivamente un elemento di maggioranza nella seconda metà
    x2 = maggioranza(V, mid + 1, end)

    # Calcola il numero di occorrenze di x1 e x2 in V
    n1, n2 = 0, 0
    for i in range(n):
        if x1 == V[i]:
            n1 += 1
        elif x2 == V[i]:
            n2 += 1

    # Restituisci l'elemento di maggioranza basato sul conteggio delle occorrenze
    if n1 >= n2:
        return x1
    else:
        return x2


def count_occurrences(V, element, j):
    count = 0
    if V[element] == V[j]:
        count += 1
    return count


def maggioranza_lineare(a):
    score = 0
    candidato = -1
    n = len(a)
    for i in range(n):
        if score == 0:
            candidato = i
            score += 1
        elif q(a, i, candidato):
            score += 1
        else:
            score -= 1
    return candidato


def q(a, i, j):
    if a[i] == a[j]:
        return True
    else:
        return False


# Esempio di utilizzo
V = [2, 4, 4, 4, 4, 7, 4, 2, 2]
n = len(V)
majority_element = maggioranza(V, 0, n - 1)
print("Elemento di maggioranza:(tempo O(nlog(n)))", majority_element)
# a = [1,5,6,7,1,4,6,8]
print("Indice dell'elemento di maggioranza:(tempo O(n))", maggioranza_lineare(V))
