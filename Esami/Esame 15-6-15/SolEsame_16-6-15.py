class TreeNode:
    def __init__(self,val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

def Alg(root,h):
    if root == None:
        return 0
    if h <= 0:
        return min(root.val,Alg(root.left,h),Alg(root.right,h))
    else:
        return min(Alg(root.left,h-1),Alg(root.right,h-1))

nodo1 = TreeNode(1)
nodo2 = TreeNode(2)
nodo3 = TreeNode(3)
nodo4 = TreeNode(4)
nodo5 = TreeNode(5)
nodo6 = TreeNode(6)
nodo7 = TreeNode(7)
nodo8 = TreeNode(-1)
#nodo9 = TreeNode(0)


nodo1.left = nodo2
nodo1.right = nodo3
nodo2.left = nodo4
nodo2.right = nodo5
nodo3.left = nodo6
nodo3.right = nodo7
nodo4.left = nodo8
# nodo8.left = nodo9

print(Alg(nodo1,2))
