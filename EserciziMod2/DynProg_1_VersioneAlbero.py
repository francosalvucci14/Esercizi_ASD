"""
L'algoritmo non funziona sempre, caso in cui non funziona = albero con 3 nodi, e radice = nodo di valore massimo
"""


class TreeNode:
    def __init__(self, val, left=None, right=None, center=None):
        self.val = val
        self.left = left
        self.right = right
        self.center = center


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def BFS(root, V):
    c = Queue()
    c.enqueue(root)
    while not c.isEmpty():
        u = c.dequeue()
        if u != None:
            # print(u.val)#visito il nodo u
            # print(u.val,"-->",root.val)
            V.append(u.val)
            c.enqueue(u.left)
            c.enqueue(u.right)
            c.enqueue(u.center)
    return V


# def BFS(root,V):
#     c = []
#     c.append(root)
#     while len(c)>0:
#         u = c.pop()
#         if u != None:
#             V.append(u.val)
#             c.append(u.right)
#             c.append(u.left)
#     return V


def MaxIS_Tree(V):
    n = len(V)
    OPT = [0] * n
    OPT[0] = V[0]
    OPT[1] = max(V[0], V[1])

    for i in range(2, n):
        OPT[i] = max(OPT[i - 1], V[i] + OPT[i - 2])
    print(OPT)
    return OPT[n - 1], OPT


V = []
root = TreeNode(2)
l1 = TreeNode(7)
r1 = TreeNode(6)
l2 = TreeNode(3)
l2_r2 = TreeNode(1)
r1_l1 = TreeNode(2)
r1_l2 = TreeNode(3)
r1_l3 = TreeNode(3)

root.left = l1
root.right = r1
l1.left = l2
l1.right = l2_r2
r1.left = r1_l1
r1.center = r1_l2
r1.right = r1_l3

V_pop = BFS(root, V)
print(V_pop)
print(MaxIS_Tree(V_pop))
