class Node:
    def __init__(self, data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right


def find_min_depth_node(node,depth,count):
        
        if node == None:
            return 0,0
        
        (SD_s,nodo) = find_min_depth_node(node.left, depth + 1,count+1)
        (SD_d,nodo) = find_min_depth_node(node.right, depth + 1,count+1)
        total_count = SD_s+SD_d+count

        if depth >= total_count:
            return (total_count,node.data)
        else:
            return (total_count,nodo)
    
def nodiGenProf(root,p,ant_min):
    if root.left == None and root.right == None:
        if p > ant_min:
            return 1
        else:
            return 0
    s=0
    if p > ant_min:
        s=1
    if root.data < ant_min:
        ant_min = root.data
    return s+nodiGenProf(root.left,p+1,ant_min)+nodiGenProf(root.right,p+1,ant_min)

# Esempio di utilizzo
root = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
# F = Node('F')
# G = Node('G')
# H = Node('H')

root.left = B
root.right = C
B.left = D
B.right = E
# C.left = F
# C.left = G
# D.left = H

(somma,nodo) = find_min_depth_node(root,0,0)
print(nodo)
print(nodiGenProf(root,0,root.data))
