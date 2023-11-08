class TreeNode:
    def __init__(self, val, col, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.col = col

# questo è lineare


def discendenti(root, b, n, SD_b, SD_n):
    if root is None:
        return (0, 0)

    if root.left == None and root.right == None:
        if root.col == "b":
            SD_b += 1
        else:
            SD_n += 1
        if SD_b >= b and SD_n >= n:
            return 1
        else:
            return (0, 0)

    if root.col == "b":
        SD_b += 1
    else:
        SD_n += 1

    (SD_s, k_s) = discendenti(root.left, b, n, SD_b, SD_n)
    (SD_d, k_d) = discendenti(root.right, b, n, SD_b, SD_n)
    SD = SD_s+SD_d+root.val
    if SD >= b and SD >= n:
        return (SD, 1+k_s+k_d)
    else:
        return (SD, k_s+k_d)


def discendenti2(root, b, n):
    if root is None:
        return (0, 0, 0)
    
    (SB_s, SN_s, k_s) = discendenti2(root.left, b, n)
    (SB_d, SN_d, k_d) = discendenti2(root.right, b, n)

    SD_btot = SB_s+SB_d
    SD_ntot = SN_s+SN_d

    if root.col == "b":
        SD_btot += 1
    else:
        SD_ntot += 1

    if SD_btot >= b and SD_ntot >= n:
        return (SD_btot, SD_ntot, 1+k_s+k_d)
    else:
        return (SD_btot, SD_ntot, k_s+k_d)


def calcoloDisc(root):
    (i, j, k) = discendenti2(root, 1, 1)
    return k


root = TreeNode(4, "n")
l1 = TreeNode(3, "n")
r1 = TreeNode(5, "b")
l1_l = TreeNode(2, "n")
l1_r = TreeNode(4, "b")
r1_l = TreeNode(2,"n")
r1_r = TreeNode(8,"b")

root.left = l1
root.right = r1
l1.left = l1_l
l1.right = l1_r
r1.left = r1_l
r1.right = r1_r

# print(countSpecialNodes(root,1,1))
print(calcoloDisc(root))
