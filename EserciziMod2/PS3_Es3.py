import pprint as pp
import sys


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            if root.left is not None:
                print_tree(root.left, level + 1, "L--- ")
            if root.right is not None:
                print_tree(root.right, level + 1, "R--- ")


def reconstruct_tree(c, memo, i, j):
    if i == j:
        # Se i == j, si tratta di una foglia
        return TreeNode(c[i])

    # Trova il punto di divisione ottimale per il sottoalbero corrente
    min_cost = float("inf")
    optimal_k = -1
    optimal_left_max = -1
    optimal_right_max = -1

    for k in range(i, j):
        left_cost = memo[i][k]
        right_cost = memo[k + 1][j]
        internal_node_cost = left_max = max(
            c[i : k + 1]
        )  # Massimo costo delle foglie del sottoalbero sinistro
        right_max = max(
            c[k + 1 : j + 1]
        )  # Massimo costo delle foglie del sottoalbero destro
        internal_node_cost *= right_max
        total_cost = left_cost + right_cost + internal_node_cost
        if total_cost < min_cost:
            min_cost = total_cost
            optimal_k = k
            optimal_left_max = left_max
            optimal_right_max = right_max

    # Ricostruisci il sottoalbero destro e sinistro, invertendo i nodi figli
    root = TreeNode(optimal_left_max * optimal_right_max)
    root.right = reconstruct_tree(c, memo, i, optimal_k)
    root.left = reconstruct_tree(c, memo, optimal_k + 1, j)
    return root


def min_cost_tree(c):
    n = len(c)
    # Inizializzazione della tabella di memoizzazione
    memo = [[-1] * n for _ in range(n)]

    # Funzione di programmazione dinamica
    def dp(i, j):
        if memo[i][j] != -1:
            return memo[i][j]

        if i == j:
            memo[i][j] = 0  # Nodo foglia, costo zero
        else:
            min_cost = float("inf")
            # Calcoliamo il costo per ogni possibile divisione in sottoalberi
            for k in range(i, j):
                left_cost = dp(i, k)
                right_cost = dp(k + 1, j)
                internal_node_cost = max(c[i : k + 1]) * max(c[k + 1 : j + 1])
                total_cost = left_cost + right_cost + internal_node_cost
                min_cost = min(min_cost, total_cost)
            memo[i][j] = min_cost
            pp.pprint(memo)
        return memo[i][j]

    # Chiamata iniziale alla funzione di programmazione dinamica
    min_cost = dp(0, n - 1)
    return min_cost, memo


# Esempio di utilizzo
# c = [1, 3, 4, 3, 2]
# c = [3, 2, 4, 5, 9]
# c = [4, 2, 9, 1, 2, 3, 10, 7]
# c = [8, 1, 3, 7, 5, 2, 9
# c = [4, 2, 9, 7, 1, 3, 2]
# c = [3, 4, 5, 1, 7, 9]
c = [1, 3, 2]
print("Istanza: ", c)
costo, opt = min_cost_tree(c)
print("Il costo minimo dell'albero binario è:", costo)
root = reconstruct_tree(c, opt, 0, len(c) - 1)

print("Albero ricostruito:")
print_tree(root)
