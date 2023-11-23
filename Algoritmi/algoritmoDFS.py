class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def DFS(root):
    S = []
    S.append(root)
    while len(S) > 0:
        u = S.pop()
        if u != None:
            print(u.val)
            S.append(u.right)
            S.append(u.left)


def DFS_postorder(root):
    if root != None:
        DFS_postorder(root.left)
        DFS_postorder(root.right)
        print(root.val)


def DFS_sim(root):
    if root != None:
        DFS_sim(root.left)
        print(root.val)
        DFS_sim(root.right)


def DFS_preorder(root):
    if root != None:
        print(root.val)
        DFS_preorder(root.left)
        DFS_preorder(root.right)


root = TreeNode("G")
h = TreeNode("H")
e = TreeNode("E")
c = TreeNode("C")
d = TreeNode("D")
a = TreeNode("A")
f = TreeNode("F")
b = TreeNode("B")

root.left = h
root.right = e
e.left = c
c.left = d
d.left = a
a.left = f
a.right = b

# DFS(root)
print("Visita in postordine")
DFS_postorder(root)
print("Visita simmetrica")
DFS_sim(root)
print("Visita in preordine")
DFS_preorder(root)

# DFS(a)
