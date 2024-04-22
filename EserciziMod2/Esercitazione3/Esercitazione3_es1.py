def palindroma_tabulation(s: str) -> int:
    n = len(s)
    M = [[0] * n for _ in range(n)]

    for i in range(n):
        M[i][i] = 1

    # il seguente ciclo for cicla le diagonali della matrice
    for d in range(1, n):
        for i in range(n - d):
            j = d + i

            if s[i] == s[j]:
                M[i][j] = 2 + M[i + 1][j - 1]
            else:
                M[i][j] = max(M[i + 1][j], M[i][j - 1])

    return M[0][n - 1]


def palindroma_memoization(s: str, i: int, j: int, cache: dict = dict()) -> int:
    if (i, j) in cache:
        return cache[i, j]

    if i > j:
        cache[i, j] = 0
    elif i == j:
        cache[i, j] = 1
    else:
        if s[i] == s[j]:
            cache[i, j] = 2 + palindroma_memoization(s, i + 1, j - 1, cache)
        else:
            cache[i, j] = max(
                palindroma_memoization(s, i + 1, j, cache),
                palindroma_memoization(s, i, j - 1, cache),
            )
    return cache[i, j]


def compute_solution(s: str, i: int, j: int, cache: dict) -> str:
    if i > j:
        return ""
    elif i == j:
        return s[i]
    else:
        if s[i] == s[j]:
            return s[i] + compute_solution(s, i + 1, j - 1, cache) + s[j]
        else:
            if cache[i + 1, j] > cache[i, j - 1]:
                return compute_solution(s, i + 1, j, cache)
            else:
                return compute_solution(s, i, j - 1, cache)


# help(palindroma_tabulation)
# help(palindroma_memoization)
# a = "ALGORITMO"
a = "otto segaci cagasotto"
opt = palindroma_tabulation(a)
print(f"Valore soluzione ottima con tabulation: {opt}")
n = len(a)
cache = dict()
opt1 = palindroma_memoization(a, 0, n - 1, cache)

print(f"Valore soluzione ottima con memoization : {opt1}")
print(f"Soluzione effettiva : {compute_solution(a,0,n-1,cache)}")
