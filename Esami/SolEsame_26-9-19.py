class TreeNode:
    def __init__(self, val, col, left=None, right=None):
        self.left = left
        self.right = right
        self.col = col
        self.val = val
# Osserviamo che ogni foglia dell'albero rispetta la condizione 
# dato che, per ogni foglia, sia he che il numero di discendenti è 0
# quindi 0>=0/2 è sempre True
def alg(root):
    if root == None:
        return 0, 0, 0
    
    n1, BL, NL = alg(root.left)
    n2, BR, NR = alg(root.right)
    
    nb = BL + BR
    nn = NL + NR
    N = n1 + n2

    if root.col == "B":
        nb += 1
    else:
        nn += 1
    
    if nb >= nn:
        N+=1
    
    return N, nb, nn


nodo1 = TreeNode(1, "N")
nodo2 = TreeNode(2, "B")
nodo3 = TreeNode(3, "B")
nodo4 = TreeNode(4, "B")
nodo5 = TreeNode(5, "N")
nodo6 = TreeNode(6, "N")
nodo7 = TreeNode(7, "N")

nodo1.left = nodo2
nodo1.right = nodo3
nodo2.left = nodo4
nodo2.right = nodo5
nodo3.left = nodo6
nodo3.right = nodo7
res, _, _ = alg(nodo1)
print(res)