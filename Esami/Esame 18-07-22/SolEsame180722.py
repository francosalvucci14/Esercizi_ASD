class TreeNode:
    def __init__(self, val,name,spec, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.name = name
        self.spec = spec
def find_special_node(node, special_node, result):
    if node is None:
        return
  
    if node == special_node or find_special_node(node.left, special_node, result) or find_special_node(node.right, special_node, result):
        result[node.name - 1] = max(result[node.name - 1], node.val)
        return True

    return False

def construct_result_vector(root, n):
    result = [0] * n
    special_nodes = []
  
    # find all special nodes
    def pre_order_traversal(node):
        if node is None:
            return

        if node.spec == "y":
            special_nodes.append(node)
  
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
  
    pre_order_traversal(root)
  
    for special_node in special_nodes:
        find_special_node(root, special_node, result)
  
    return result

root = TreeNode(4,1,"n")
l1 = TreeNode(3,2,"y")
r1 = TreeNode(5,3,"y")
l1_l = TreeNode(2,2,"n")
l1_r = TreeNode(4,3,"y")
# r1_l = TreeNode(2)
# r1_r = TreeNode(8)

root.left = l1
root.right = r1
l1.left = l1_l
l1.right = l1_r
# r1.left = r1_l
# r1.right = r1_r

print(construct_result_vector(root,5))
