import random

def find_k_smallest_numbers(n, k):
    numbers = []  # Lista per mantenere i numeri della collezione online
    k_smallest = []  # Lista per mantenere i k numeri più piccoli

    for _ in range(n):
        num = get_next_number()  # Funzione che recupera il prossimo numero nella collezione online
        numbers.append(num)

    k_smallest = quick_select(numbers, k)

    return sorted(k_smallest)

def quick_select(arr, k):
    pivot = random.choice(arr)  # Scegliamo un pivot casuale dalla lista

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    pivot_occurrences = arr.count(pivot)

    if k < len(left):
        return quick_select(left, k)
    elif k < len(left) + pivot_occurrences:
        return [pivot] * pivot_occurrences
    else:
        return quick_select(right, k - len(left) - pivot_occurrences)

# Funzione fittizia per simulare la collezione online
def get_next_number():
    # Implementare questa funzione in base al modo in cui si ottengono i numeri nella collezione online
    raise StopIteration

# Esempio di utilizzo dell'algoritmo:
n = 100  # Numero totale di numeri nella collezione online
k = int(n ** 0.5)  # k = Θ(√n)

k_smallest_numbers = find_k_smallest_numbers(n, k)
print("I", k, "numeri più piccoli della collezione sono:", k_smallest_numbers)
