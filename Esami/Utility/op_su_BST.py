class TreeNode:
    def __init__(self, val,parent = None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def Precedessore(root):
    if (root.left != None):
        return max(root.left)
    while root.parent != None and root == root.parent.left :
        root = root.parent
    return root.parent.val

def Successore(root):
    if (root.right != None):
        return min(root.right)
    while root.parent != None and root == root.parent.right :
        root = root.parent
    return root.parent.val

def Search(chiave,root):

    while(root!=None):
        if chiave == root.val:
            return root.val
        elif chiave < root.val:
            root = root.left
        else:
            root = root.right
    return None

root = TreeNode(15)
sx_r = TreeNode(6)
sx_sx_r  =TreeNode(3)
sx_sx_sx_r = TreeNode(2)
dx_sx_sx_r = TreeNode(4)
dx_sx_r = TreeNode(8)
sx_dx_sx_r = TreeNode(7)
dx_dx_sx_r = TreeNode(13)
sx_dx_dx_sx_r = TreeNode(9)
dx_r = TreeNode(18)
sx_dx_r = TreeNode(17)
dx_dx_r = TreeNode(20)

root.left = sx_r
root.right = dx_r
sx_r.left = sx_sx_r
sx_r.right = dx_sx_r
sx_sx_r.left = sx_sx_sx_r
sx_sx_r.right = dx_sx_sx_r
dx_sx_r.left = sx_dx_sx_r
dx_sx_r.right = dx_dx_sx_r
dx_dx_sx_r.left = sx_dx_dx_sx_r
dx_r.left = sx_dx_r
dx_r.right = dx_dx_r


root.parent = root
sx_r.parent = root
sx_sx_r.parent = sx_r
sx_sx_sx_r.parent = sx_sx_r
dx_sx_sx_r.parent = sx_sx_r
dx_sx_r.parent = sx_r
sx_dx_sx_r.parent = dx_sx_r
dx_dx_sx_r.parent = dx_sx_r
sx_dx_dx_sx_r.parent = dx_dx_sx_r
dx_r.parent = root
sx_dx_r.parent = dx_r
dx_dx_r.parent = dx_r 


print(Precedessore(sx_dx_dx_sx_r))
print(Successore(sx_dx_dx_sx_r))
print(Search(7,root))