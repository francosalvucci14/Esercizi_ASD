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

def BFS(root):
    c = Queue()
    c.enqueue(root)
    while not c.isEmpty():
        u = c.dequeue()
        if u != None:
            #print(u.val)#visito il nodo u
            print(u.val,"-->",root.val)
            c.enqueue(u.left)
            c.enqueue(u.right)

# def BFS(root): senza la classe Queue
#     c = []
#     c.append(root)
#     while len(c)>0:
#         u = c.pop()
#         if u != None:
#             print(u.val)
#             c.append(u.right)
#             c.append(u.left)

root = TreeNode("A")
l1 = TreeNode("L")
r1 = TreeNode("B")
l2 = TreeNode("E")
r2 = TreeNode("R")
r3 = TreeNode("O")

root.left = l1
l1.right = r1
r1.left = l2
l2.right = r2
r2.right = r3

BFS(root)
