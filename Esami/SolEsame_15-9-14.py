from collections import deque

class TreeNode:
    def __init__(self,col, left=None, right=None):
        self.left = left
        self.right = right
        self.col = col


def hasBlackLevel(root,a):
    if root is None:
        return False

    queue = deque()
    queue.append(root)
    currentLevel = 0
    blackLevelFound = False

    while queue:
        levelSize = len(queue)
        currentLevelHasBlackNodes = True

        for _ in range(levelSize):
            node = queue.popleft()

            if node.col != 'Nero':
                currentLevelHasBlackNodes = False

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        if currentLevelHasBlackNodes:
            blackLevelFound = True
            a[currentLevel] = 1 # se si usa la versione con array lasciare, altrimenti commentare
            #break

        currentLevel += 1

    return blackLevelFound

     
def AlgoritmoLivelloNero(root,h):# Versione con array per indicare i livelli neri
    a = [0]*h #h = altezza albero
    hasBlackLevel(root,a)
    
    print(a)
    
    for i in range(h):
        if a[i] == 1:
            print(f"Livelli neri : {i}")
            #return True
    #return False

nodo1 = TreeNode('Bianco')
nodo2 = TreeNode('Nero')
nodo3 = TreeNode('Nero')
nodo4 = TreeNode('Nero')
nodo5 = TreeNode('Nero')
nodo6 = TreeNode('Nero')
#nodo7 = TreeNode('Nero')


nodo1.left = nodo2
nodo1.right = nodo3
nodo2.left = nodo4
nodo2.right = nodo5
nodo3.left = nodo6
#nodo3.right = nodo7

#print(hasBlackLevel(nodo1))
print(AlgoritmoLivelloNero(nodo1,3))