
#soluzione esame 14-9-22
class TreeNode:
    def __init__(self, val,col, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.col = col
def DFS(root,b,n,sn,sb):
    S = []
    S.append(root)
    #print(root.val)
    #print(f"Contatore bianchi {cb}, contatore neri {cn} per il nodo {root.val},{root.col}")
    if root.left == None and root.right == None:
        if sn >= n and sb>=b:
            print(root.val)
            return 1
        else:
            return 0
    s = 0
    if sn >= n and sb>=b:
        s=1
        print(root.val)
    if root.col == "b":
        sb+=1
    else:
        sn+=1
        
    return s+DFS(root.left,b,n,sn,sb)+DFS(root.right,b,n,sn,sb)
def antenati(root):
    S = []
    S.append(root)
    radice = S[0]
    #print(radice.val)
    b=0
    n=1
    #colore = radice.col
    num_antenati = DFS(radice,b,n,0,0)
    print(f"num antenati {num_antenati}")
    

# root = TreeNode(1,"b") #b
# l1 = TreeNode(5,"n")#n
# r1 = TreeNode(3,"b")#b
# l1_l1 = TreeNode(3,"b")#b
# l1_r1 = TreeNode(4,"b")#b
# l1_r1_l1 = TreeNode(1,"n")
# l1_r1_r1 = TreeNode(2,"b")
# r1_l1 = TreeNode(2,"n")
# r1_r1 = TreeNode(4,"n")
# r1_r1_l1 = TreeNode(1,"n")
# r1_r1_r1 = TreeNode(3,"b")

# root.left = l1
# root.right = r1
# l1.left = l1_l1
# l1.right = l1_r1
# l1_r1.left = l1_r1_l1
# l1_r1.right = l1_r1_r1
# r1.left = r1_l1
# r1.right = r1_r1
# r1_r1.left = r1_r1_l1
# r1_r1.right = r1_r1_r1

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
antenati(root)