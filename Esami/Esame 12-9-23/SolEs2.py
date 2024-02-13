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

def Alg(root,h1,h2,p):
    if root == None:
        return 0
    if root.left != None or root.right != None:
        if p>=h1 and p<=h2:
            return 1+Alg(root.left,h1,h2,p+1)+Alg(root.right,h1,h2,p+1)
        else:
            return Alg(root.left,h1,h2,p+1)+Alg(root.right,h1,h2,p+1)
    else:
        return 0

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
nodo4.left = nodo8
# nodo8.left = nodo9
h1=1
h2=3
print(Check(nodo1,h1,h2))