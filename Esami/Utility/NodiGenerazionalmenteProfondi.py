class TreeNode:
    def __init__(self,val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def nodiGenProf(root,p,ant_min):
    if root.left == None and root.right == None:
        if p > ant_min:
            return 1
        else:
            return 0
    s=0
    if p > ant_min:
        s=1
    if root.val < ant_min:
        ant_min = root.val
    return s+nodiGenProf(root.left,p+1,ant_min)+nodiGenProf(root.right,p+1,ant_min)

nodo1 = TreeNode(0)
nodo2 = TreeNode(1)
nodo3 = TreeNode(5)
nodo4 = TreeNode(2)
nodo5 = TreeNode(4)
# nodo6 = TreeNode(2)
# nodo7 = TreeNode(8)

nodo1.left = nodo2
nodo1.right = nodo3
nodo2.left = nodo4
nodo2.right = nodo5
# nodo3.left = nodo6
# nodo3.right = nodo7
 
print(nodiGenProf(nodo1,0,nodo1.val))
