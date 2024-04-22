import pprint as pp
from colorama import Fore, Style


def scaffali_memoization(i: int, w: int, a: list, cache: dict) -> int:
    if i == 0:
        return 0

    if (i, w) in cache:
        return cache[i, w]

    if a[i - 1] > w:
        cache[i, w] = a[i - 1] + scaffali_memoization(i - 1, w, a, cache)
    else:
        cache[i, w] = min(
            a[i - 1] + scaffali_memoization(i - 1, w, a, cache),
            scaffali_memoization(i - 1, w - a[i - 1], a, cache),
        )

    return cache[i, w]


def find_minimum_W(n: int, a: list, W: int) -> int:
    cache = dict()
    max_W = sum(a)
    for W in range(W, max_W + 1):
        if scaffali_memoization(n, W, a, cache) <= W:
            return W


input = [2, 1, 2, 2, 1, 1, 2, 1, 4, 1, 3, 1]
w = 0
# print(f"Soluzione ottima : {scaffali_tabulation(input,w)}") DA FARE
n = len(input)
print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + f"Istanza del problema : {input}")
print(
    "Soluzione ottima con memoization:" + Fore.RED + f" W = {find_minimum_W(n,input,w)}"
)
