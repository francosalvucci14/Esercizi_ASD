
# soluzione esame 14-9-22
class TreeNode:
    def __init__(self, val, col, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.col = col


def DFS(root, k, sn):
    S = []
    S.append(root)
    # print(root.val)
    if root.col == "n":
        sn += 1
    # print(f"Contatore bianchi {cb}, contatore neri {cn} per il nodo {root.val},{root.col}")
    if root.left == None and root.right == None:
        if sn <= k:
            
            return 1
        else:
            return 0

    return DFS(root.left, k, sn)+DFS(root.right, k, sn)


def antenati(root):
    S = []
    S.append(root)
    radice = S[0]
    # print(radice.val)
    k = 2
    # colore = radice.col
    check = DFS(radice, k, 0)
    if check >= 1:
        cammino=True
    else:
        cammino=False
    print(f"Esiste un cammino radice-foglia con al più {k} nodi neri? {cammino}")


root = TreeNode(1, "n")
l1 = TreeNode(2, "n")
r1 = TreeNode(3, "b")
l1_l = TreeNode(5, "b")
l1_r = TreeNode(6, "n")
r1_l = TreeNode(7,"b")
r1_r = TreeNode(8,"n")

root.left = l1
root.right = r1
l1.left = l1_l
l1.right = l1_r
r1.left = r1_l
r1.right = r1_r


antenati(root)
