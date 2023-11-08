"""
AntBenCol(v,C)
- restituisce in output il numero di nodi con antenati ben colorati nel sottoalbero radicato in v;
- prende in input:
-- il nodo v;
-- il colore C \in {B,G} che "si aspetta di vedere". Se C=B vuol dire che fino a v (v escluso) ho visto solo antenati di colore Blu, se C=G vuol dire che nella sequenza di antenati fino a v (v escluso) ho visto almeno un antenato Giallo.

AntBenCol(v,C)
if v=null then return 0;
if C=G and v.col=B then return 0;
//qui ho che C=B
if v.col=G then C=G;
return 1+AntBenCol(v.sx,C)+AntBenCol(v.dx,C);

la chiamata iniziale è: AntBenCol(radice,B);
"""

class TreeNode:
    def __init__(self,val,col, left=None, right=None):
        self.left = left
        self.right = right
        self.col = col
        self.val = val


def AntBenCol(root,C):
    if root == None:
        return 0
    if C == "Giallo" and root.col == "Blu":
        return 0
    if root.col == "Giallo":
        C="Giallo"
        
    return 1+AntBenCol(root.left,C)+AntBenCol(root.right,C)


nodo1 = TreeNode(1,'Blu')
nodo2 = TreeNode(2,'Giallo')
nodo3 = TreeNode(3,'Blu')
nodo4 = TreeNode(4,'Blu')
nodo5 = TreeNode(5,'Blu')
nodo6 = TreeNode(6,'Giallo')
nodo7 = TreeNode(7,'Giallo')


nodo1.left = nodo2
nodo1.right = nodo3
nodo2.left = nodo4
nodo2.right = nodo5
nodo5.left = nodo6
nodo3.left = nodo7
 
print(AntBenCol(nodo1,"Blu"))
