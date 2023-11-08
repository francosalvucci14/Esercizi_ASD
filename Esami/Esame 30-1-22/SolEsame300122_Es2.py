class TreeNode:
    def __init__(self,col, left=None, right=None):
        self.left = left
        self.right = right
        self.col = col
def countYellowNodeAtHDeapth(root, p, h):
    S = []
    S.append(root)
    if root == None:
        return 0
    if root.left == None and root.right == None:
        if root.col == "y" and p>=h:
            return 1
        else:
            return 0
    
    return countYellowNodeAtHDeapth(root.left,p+1,h)+countYellowNodeAtHDeapth(root.right,p+1,h)


root = TreeNode("n")
l1 = TreeNode("y")
r1 = TreeNode("y")
l1_l = TreeNode("n")
l1_r = TreeNode("y")
r1_l = TreeNode("y")
r1_r = TreeNode("y")

root.left = l1
root.right = r1
l1.left = l1_l
l1.right = l1_r
r1.left = r1_l
r1.right = r1_r

print(countYellowNodeAtHDeapth(root,0,2))
