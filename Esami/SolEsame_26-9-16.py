class TreeNode:
    def __init__(self,val,col, left=None, right=None):
        self.left = left
        self.right = right
        self.col = col
        self.val = val

def SommaBianchiUgualeSommaNeri(root,sb,sn):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        if sn == sb:
            return 1
        else:
            return 0
    s = 0
    if sn == sb:
        s=1
    if root.col == "Bianco":
        sb = sb+1
    else:
        sn = sn+1
    return s+SommaBianchiUgualeSommaNeri(root.left,sb,sn)+SommaBianchiUgualeSommaNeri(root.right,sb,sn)

nodo1 = TreeNode(1,'Nero')
nodo2 = TreeNode(2,'Bianco')
nodo3 = TreeNode(3,'Nero')
nodo4 = TreeNode(4,'Nero')
nodo5 = TreeNode(5,'Nero')
nodo6 = TreeNode(6,'Bianco')
nodo7 = TreeNode(7,'Bianco')


nodo1.left = nodo2
nodo1.right = nodo3
nodo2.left = nodo4
nodo2.right = nodo5
nodo3.left = nodo6
nodo3.right = nodo7

print(SommaBianchiUgualeSommaNeri(nodo1,0,0))