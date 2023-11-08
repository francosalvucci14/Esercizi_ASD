class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    # Il primo elemento della sequenza preordine è la radice
    root_data = preorder[0]
    root = Node(root_data)
    
    # Troviamo l'indice del nodo radice nella sequenza inorder
    root_index = inorder.index(root_data)
    
    # Ricostruiamo i sottoalberi in modo ricorsivo
    left_preorder = preorder[1:root_index + 1]
    left_inorder = inorder[:root_index]
    root.left = build_tree(left_preorder, left_inorder)
    
    right_preorder = preorder[root_index + 1:]
    right_inorder = inorder[root_index + 1:]
    root.right = build_tree(right_preorder, right_inorder)
    
    return root

def VisitaSimmetrica(root):
    if root != None:
        VisitaSimmetrica(root.left)
        print(root.data)
        VisitaSimmetrica(root.right)

def VisitaPreorder(root):
    if root != None:
        print(root.data)
        VisitaPreorder(root.left)
        VisitaPreorder(root.right)
    
# Esempio di utilizzo con i dati forniti
preorder = ['G', 'H', 'E', 'C', 'D', 'A', 'F', 'B']
inorder = ['H', 'G', 'F', 'A', 'B', 'D', 'C', 'E']

tree = build_tree(preorder, inorder)

print(VisitaSimmetrica(tree))
print(VisitaPreorder(tree))