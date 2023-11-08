class Node:
    def __init__(self, data,col,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        self.col = col

def MaxRosso(root):
    if root == None:
        return 0
    if root.col == "N":
        return 0
    return root.data+max(MaxRosso(root.left),MaxRosso(root.right))

def Bilanciati(root,SA):
    if root == None:
        return (0,0)
    SA = SA+root.data
    (SD_s,k_s) = Bilanciati(root.left,SA)
    (SD_d,k_d) = Bilanciati(root.right,SA)
    SD = SD_s+SD_d+root.data
    if SA == SD:
        return (SD,1+k_d+k_s)
    else:
        return (SD,k_d+k_s)

def Profondità(root,p,h):
    if root == None:
        return 0
    if p >= h:
        return 1+Profondità(root.left,p+1,h)+Profondità(root.right,p+1,h)
    else:
        return Profondità(root.left,p+1,h)+Profondità(root.right,p+1,h)

root = Node(3,"R")
l1 = Node(10,"R")
r1 = Node(4,"R")
l2 = Node(1,"R")
r2 = Node(2,"R")
l3 = Node(15,"R")
r3 = Node(20,"N")

root.left = l1
root.right = r1
l1.left = l2
l1.right = r2
r1.left = l3
r1.right = r3

print(MaxRosso(root))
(SD,k) = Bilanciati(root,0)
print(k)
print(Profondità(root,0,1))