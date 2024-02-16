class TreeNode:
    def __init__(self,val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

def Check(root,h1,h2):
    if h1>h2:
        return -1
    p=0
    
    return Alg(root,h1,h2,p)

def Alg(root,delta,SA):
    if root == None:
        return (0,delta,0)
    SA = SA+root.val
    (sx,delta,ks) = Alg(root.left,delta,SA)
    (dx,delta,kd) = Alg(root.right,delta,SA)
    tot = sx+dx
    if SA>=delta:
        return (tot,delta,1+ks+kd)
    else:
        return (tot,delta,ks+kd)

nodo1 = TreeNode(1)
nodo2 = TreeNode(2)
nodo3 = TreeNode(5)
nodo4 = TreeNode(8)
nodo5 = TreeNode(3)
nodo6 = TreeNode(15)
nodo7 = TreeNode(4)
nodo8 = TreeNode(7)
nodo9 = TreeNode(6)


nodo1.left = nodo2
nodo1.right = nodo3
nodo2.left = nodo4
nodo2.right = nodo5
nodo3.left = nodo6
nodo3.right = nodo7
nodo4.left = nodo8
nodo4.right = nodo9

nodi,delta,nodi_condizione = Alg(nodo1,5,0)
print(nodi_condizione)