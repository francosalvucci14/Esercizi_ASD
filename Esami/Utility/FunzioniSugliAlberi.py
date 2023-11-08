class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def CalcolaAltezza(root):
    if root == None:
        return -1
    dx = CalcolaAltezza(root.right)
    sx = CalcolaAltezza(root.left)
    return 1+max(sx,dx)
def CercaElemento(r,k):
    if r==None:
        return None
    if r.val == k:
        return r.val
    sx = CercaElemento(r.left,k)
    if sx != None:
        return sx
    return CercaElemento(r.right,k)
def CalcolaNumFoglie(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    sx = CalcolaNumFoglie(root.left)
    dx = CalcolaNumFoglie(root.right)
    return (sx+dx)
def CalcoloGradoMedio(root):
    n=7
    nfoglie = CalcolaNumFoglie(root)
    return (SommaGradi(root)/n-nfoglie)
def SommaGradi(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    S = 7+SommaGradi(root.left)+SommaGradi(root.right)
    return S
root = TreeNode("A")
l1 = TreeNode("L")
l2 = TreeNode("E")
r1 = TreeNode("R")
r2 = TreeNode("B")
r3 = TreeNode("O")
r4 = TreeNode("RR")

root.left = l1
root.right = r2
l1.left = l2
l1.right = r1
r2.right = r3
r1.right = r4
# root = TreeNode(3)
# l1 = TreeNode(2)
# r1 = TreeNode(1)
# r_l1_1 = TreeNode(1)
# r_l1_1_1 = TreeNode(0)
# l_l1_1_1 = TreeNode(0)
# r_r1 = TreeNode(0)

# root.right = r1
# r1.right = r_r1
# root.left = l1
# l1.right = r_l1_1
# r_l1_1.right = r_l1_1_1
# r_l1_1.left = l_l1_1_1
h = CalcolaAltezza(root)
print(h)
n = CercaElemento(root,"L")
print(n)
nf = CalcolaNumFoglie(root)
print(nf)
g = CalcoloGradoMedio(root)
print(g)