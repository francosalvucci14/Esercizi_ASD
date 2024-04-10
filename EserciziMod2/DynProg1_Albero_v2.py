import sys
class TreeNode:
    def __init__(
        self,
        val,
        left=None,
        center=None,
        right=None,
        root=None,
        deep=None,
        max=None,
        mark=None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.center = center
        self.root = root
        self.deep = deep
        self.max = max
        self.mark = mark


def Algoritmo(nodo):
    opt = MaxIS_Tree(nodo)
    return opt[2]


def MaxIS_Tree(nodo):
    if nodo == None:
        return 0, 0, 0
    if nodo.left == None and nodo.right == None:
        nodo.root = nodo.val
        nodo.deep = 0
        nodo.max = nodo.val
        
        return nodo.root, nodo.deep, nodo.max
    _, opt_figli_l, opt_max_l = MaxIS_Tree(nodo.left)
    _, opt_figli_r, opt_max_r = MaxIS_Tree(nodo.right)
    _, opt_figli_c, opt_max_c = MaxIS_Tree(nodo.center)
    nodo.root = nodo.val + (opt_figli_l + opt_figli_r + opt_figli_c)
    nodo.deep = opt_max_r + opt_max_l + opt_max_c
    nodo.max = max(nodo.root, nodo.deep)
    return nodo.root, nodo.deep, nodo.max


def Ric(nodo):
    max = Algoritmo(nodo)
    if nodo.root == max:
        print(f"Nodo che fa parte della soluzione : {nodo.val}")
        Ricostruzione(nodo.left, True)
        Ricostruzione(nodo.right, True)
        Ricostruzione(nodo.center,True)
    else:
        Ricostruzione(nodo.left, False)
        Ricostruzione(nodo.right, False)
        Ricostruzione(nodo.center,False)


def Ricostruzione(nodo, bool):
    if nodo == None:
        return None
    if bool == True:
        Ricostruzione(nodo.left,False)
        Ricostruzione(nodo.right,False)
        Ricostruzione(nodo.center,False)
    else:
        if nodo.root == nodo.max:
            nodo.mark=True
            print(f"Nodo che fa parte della soluzione : {nodo.val}")
            Ricostruzione(nodo.left,True)
            Ricostruzione(nodo.right,True)
            Ricostruzione(nodo.center,True)
        else:
            Ricostruzione(nodo.left,False)
            Ricostruzione(nodo.right,False)
            Ricostruzione(nodo.center,False)

def printTree(root, level=0):
    if root == None:
        return None
    if level == 0:
        label="Radice"
    elif root.left != None or root.right != None:
        label = "Nodo interno"
    else:
        label = "Foglia"
    tee = "├──"
    elbow = "└──"
    pipe = "│"
    print('|_\t'* level + str(root.val)+" "+label)
    sx = printTree(root.left,level + 1)
    dx = printTree(root.right,level + 1)
    cx = printTree(root.center,level + 1)

def print_tree(node, indent="", last=True, parent=None):
    """
    Stampa l'albero a partire dal nodo specificato con etichette per ogni tipo di nodo.

    Args:
        node (TreeNode): Il nodo radice dell'albero da stampare.
        indent (str): L'indentazione corrente per questo livello di nodo.
        last (bool): True se questo è l'ultimo nodo figlio, False altrimenti.
        parent (TreeNode): Il genitore del nodo attuale.
    """
    if node is not None:
        sys.stdout.write(indent)
        if last:
            sys.stdout.write("└─")
            new_indent = indent + "  "
        else:
            sys.stdout.write("├─")
            new_indent = indent + "│ "

        node_type = ""
        if parent is None:
            node_type = "Radice"
        elif node.left is None or node.right is None:
            node_type = "Foglia"
        else:
            node_type = "Nodo interno"

        sys.stdout.write(f"{node.val} {node_type}\n")

        children = [node.left, node.center, node.right]
        for i, child in enumerate(children):
            print_tree(child, new_indent, i == 2, node)

root = TreeNode(2)
l1 = TreeNode(7)
r1 = TreeNode(6)
l2 = TreeNode(3)
l2_r2 = TreeNode(1)
r1_l1 = TreeNode(2)
r1_l2 = TreeNode(3)
r1_l3 = TreeNode(3)

root.left = l1
root.right = r1
l1.left = l2
l1.right = l2_r2
r1.left = r1_l1
r1.center = r1_l2
r1.right = r1_l3

#Prove Albero
# root = TreeNode(5)
# l1 = TreeNode(1)
# r1 = TreeNode(8)
# l1_r1 = TreeNode(4)
# l1_l1 = TreeNode(5)
# l1_c1 = TreeNode(6)

# root.left = l1
# root.right = r1
# l1.left = l1_l1
# l1.center = l1_c1
# l1.right = l1_r1
    
# root = TreeNode(5)
# l1 = TreeNode(1)
# l2 = TreeNode(8)
# l3 = TreeNode(9)
# l4 = TreeNode(0)
# l5 = TreeNode(11)

# root.left=l1
# l1.left = l2
# l2.left = l3
# l3.left = l4
# l4.left = l5

print("\nIstanza :")
#printTree(root)
print_tree(root)

print(f"Soluzione ottima del problema : {Algoritmo(root)}")
Ric(root)


