class TreeNode:
    def __init__(self,val,col, left=None, right=None):
        self.left = left
        self.right = right
        self.col = col
        self.val = val

def alg(root,p,h,sn,sb):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        if sn > sb and p>=h:
            print(root.val) #and root.col == "n":
            return 1
        else:
            return 0
    s=0
    if sn > sb and p>=h:# and root.col == "n":
        s=1
        print(root.val)
    if root.col == "b":
        sb+=1
    else:
        sn+=1
    return s+alg(root.left,p+1,h,sn,sb)+alg(root.right,p+1,h,sn,sb)


root = TreeNode(1,"n")
l1 = TreeNode(2,"b")
r1 = TreeNode(3,"n")
l1_l = TreeNode(4,"n")
l1_r = TreeNode(5,"n")
r1_l = TreeNode(6,"b")
r1_r = TreeNode(7,"n")

root.left = l1
root.right = r1
l1.left = l1_l
l1.right = l1_r
r1.left = r1_l
r1.right = r1_r

print(f"Numero di nodi {alg(root,0,0,0,0)}")

