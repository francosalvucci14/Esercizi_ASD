class TreeNode:
    def __init__(self, val,col, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.col = col
def DFS(root,min_ant,p):
    S = []
    S.append(root)
    #print(root.val)
    #print(f"Contatore bianchi {cb}, contatore neri {cn} per il nodo {root.val},{root.col}")

    if root.left == None and root.right == None:
        if p>min_ant:
            return 1
        else:
            return 0
    s = 0
    # sto vedendo un nodo interno
    if p>min_ant:
        s=1
    if root.val < min_ant:
        #s = 1
        min_ant = root.val
    return s+DFS(root.left,min_ant,p+1)+DFS(root.right,min_ant,p+1)
def antenati(root):
    S = []
    S.append(root)
    radice = S[0]
    
    num_antenati = DFS(radice,radice.val,0)
    print(f"num nodi generazionalmente profondi :  {num_antenati}")
    

root = TreeNode(4,"n")
l1 = TreeNode(1,"n")
r1 = TreeNode(5,"b")
l1_l = TreeNode(2,"n")
l1_r = TreeNode(4,"b")
r1_l = TreeNode(2,"b")
r1_r = TreeNode(8,"n")

root.left = l1
root.right = r1
l1.left = l1_l
l1.right = l1_r
r1.left = r1_l
r1.right = r1_r

antenati(root)