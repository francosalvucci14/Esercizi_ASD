
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
        if sn >= n or sb>=b:
            return 1
        else:
            return 0
    s = 0
    if sn >= n or sb>=b:
        s = 1
    if root.col == "b":
        sb = sb+1
    else:
        sn = sn+1
        
    return s+DFS(root.left,b,n,sn,sb)+DFS(root.right,b,n,sn,sb)
def antenati(root):
    S = []
    S.append(root)
    radice = S[0]
    #print(radice.val)
    b=3
    n=1
    
    num_antenati = DFS(radice,b,n,0,0)
    print(f"num antenati {num_antenati}")
    

root = TreeNode(1,"b") #b
l1 = TreeNode(5,"n")#n
r1 = TreeNode(3,"b")#b
l1_l1 = TreeNode(3,"b")#b
l1_r1 = TreeNode(4,"b")#b
l1_r1_l1 = TreeNode(1,"n")
l1_r1_r1 = TreeNode(2,"b")
r1_l1 = TreeNode(2,"n")
r1_r1 = TreeNode(4,"n")
r1_r1_l1 = TreeNode(1,"n")
r1_r1_r1 = TreeNode(3,"b")

root.left = l1
root.right = r1
l1.left = l1_l1
l1.right = l1_r1
l1_r1.left = l1_r1_l1
l1_r1.right = l1_r1_r1
r1.left = r1_l1
r1.right = r1_r1
r1_r1.left = r1_r1_l1
r1_r1.right = r1_r1_r1

antenati(root)