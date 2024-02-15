class TreeNode:
    def __init__(self,val, left=None, right=None,special=None):
        self.left = left
        self.right = right
        self.val = val
        self.special = special

def Alg(root,special,V):
    if root == None:
        return 0
    if root.special == True:
        special = root.val
    sx = Alg(root.left,special,V)
    dx = Alg(root.right,special,V)
    if root.special == True:
        V[root.val] = root.val
        print(V[1:])
        return root.val
    else:
        m = max(special,dx,sx)
        V[root.val] = m
        print(V[1:])
        return max(dx,sx)
    
nodo1 = TreeNode(1)
nodo2 = TreeNode(2)
nodo3 = TreeNode(3)
nodo4 = TreeNode(4)
nodo5 = TreeNode(5)
nodo6 = TreeNode(6)
nodo7 = TreeNode(7)
nodo8 = TreeNode(8)
#nodo9 = TreeNode(0)


nodo1.left = nodo2
nodo1.right = nodo3
nodo2.left = nodo4
nodo2.right = nodo5
nodo3.left = nodo6
nodo3.right = nodo7
#nodo4.left = nodo8

nodo1.special = False
nodo2.special = True
nodo3.special = False
nodo4.special = False
nodo5.special = False
nodo6.special = True
nodo7.special = False
#nodo8.special = True

# nodo8.left = nodo9
V = [0]*8
print(Alg(nodo1,0,V))