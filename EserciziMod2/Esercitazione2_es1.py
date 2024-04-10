def calculate_optimal_value(L, G):
    Opt = [0] * (L + 1)
    for j in range(1, L + 1):
        max_value = 0
        for k in range(j):
            max_value = max(max_value, G[j - k] + Opt[k])
        Opt[j] = max_value

    print(Opt)

    return Opt[L]


def calculate_optimal_value_with_solution(L, G):
    Opt = [(0, []) for _ in range(L + 1)]
    for j in range(1, L + 1):
        max_value = 0
        optimal_indices = []
        for k in range(j):
            # if G[j - k] + Opt[k][0] > max_value:
            #     max_value = G[j - k] + Opt[k][0]
            #     optimal_indices = Opt[k][1] + [j - k]
            max_value = max(max_value,G[j-k]+Opt[k][0])
            if max_value == G[j-k]+Opt[k][0]:
                optimal_indices = Opt[k][1]+[j-k]
        Opt[j] = (max_value, optimal_indices)

    print(Opt)

    return Opt[L]


L = 7  # Lunghezza dell'array
G = [
    0,
    6,
    10,
    20,
    21,
    25,
    28,
    30,
]  # Valori associati agli indici (G[0] è solo un segnaposto)
sol_ottima, soluzione = calculate_optimal_value_with_solution(L, G)
print("Risultato ottimale:", sol_ottima)
print("Soluzione:", soluzione)
