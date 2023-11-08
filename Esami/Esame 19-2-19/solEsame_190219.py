class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def SommaNodiPerLivello(root,delta):
    C = Queue()
    C.enqueue(root)
    somma_lv = 0
    while not C.isEmpty():
        u = C.dequeue()
        if u != None:
            somma_lv+=u.val
            C.enqueue(u.left)
            C.enqueue(u.right)
        if C.isEmpty():
            if somma_lv >= delta:
                return True
            else:
                somma_lv = 0
                return False

nodo1 = TreeNode(1)
nodo2 = TreeNode(2)
nodo3 = TreeNode(3)
nodo4 = TreeNode(4)
nodo5 = TreeNode(5)
nodo6 = TreeNode(6)
nodo7 = TreeNode(7)


nodo1.left = nodo2
nodo1.right = nodo3
nodo2.left = nodo4
nodo2.right = nodo5
nodo5.left = nodo6
nodo3.left = nodo7

print(SommaNodiPerLivello(nodo1,50))