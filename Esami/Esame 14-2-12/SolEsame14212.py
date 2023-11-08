class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def node_deapth(root,p):
    
    S = []
    S.append(root)
    if root == None:
        return 0
    if root.left == None and root.right == None:
        if root.val == p:
            return 1
        else:
            return 0
    count = 0
    if root.val == p:
        count = 1
    return count+node_deapth(root.left,p+1)+node_deapth(root.right,p+1)

# versione equivalente
def Alg(root,p):
    if root == None:
        return 0
    sx = Alg(root.left,p+1)
    dx = Alg(root.right,p+1)
    if root.val == p:
        return 1+sx+dx
    else:
        return sx+dx
    
root = TreeNode(5)
l1 = TreeNode(4)
r1 = TreeNode(3)
l1_l = TreeNode(2)
l1_r = TreeNode(7)
r1_l = TreeNode(2)
r1_r = TreeNode(2)
l1_l_l = TreeNode(3)

root.left = l1
root.right = r1
l1.left = l1_l
l1.right = l1_r
r1.left = r1_l
r1.right = r1_r
l1_l.left = l1_l_l

print(node_deapth(root,0))
print(Alg(root,0))
