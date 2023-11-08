import random

#a = [100,5]
#a = [5,8,7,100,56,41,99,5,82,41]
a = [3,5,30,48,2]

# Definizione dell'algoritmo di counting sort
def counting_sort(arr, max_value):
    n = len(arr)
    count = [0] * (max_value + 1)
    output = [0] * n

    # Fase di conteggio delle occorrenze di ciascun elemento
    for num in arr:
        count[num] += 1

    # Fase di calcolo delle posizioni finali degli elementi ordinati
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Fase di ordinamento effettivo
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

# Definizione dell'algoritmo di ordinamento lineare per A
def linear_sort(A):
    n = len(A)
    max_value = 10 * n

    # Dimensione dei blocchi
    block_size = int(n**(2/3))

    # Dividiamo A in blocchi e ordiniamo ciascun blocco
    sorted_blocks = [counting_sort(A[i:i+block_size], max_value) for i in range(0, n, block_size)]

    # Uniamo i blocchi ordinati utilizzando l'ordinamento merge
    sorted_A = sorted_blocks[0]

    for i in range(1, len(sorted_blocks)):
        sorted_A = merge(sorted_A, sorted_blocks[i])

    return sorted_A

# Definizione dell'algoritmo di ordinamento merge
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Esempio di utilizzo dell'algoritmo di ordinamento lineare
#A = [4, 7, 2, 9, 1, 8, 5, 6, 3]
sorted_A = linear_sort(a)
print(sorted_A)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]



