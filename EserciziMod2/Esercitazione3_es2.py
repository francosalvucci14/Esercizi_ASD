def scaffali(a: list) -> int:
    """
    Problema simile alll scheduling dei processi
    """
    n = len(a)
    M = [[0] * n for _ in range(n)]
    return 0


input = [2, 1, 2, 2, 1, 1, 2, 1, 4, 1, 3, 1]
print(f"Soluzione ottima : {scaffali(input)}")
