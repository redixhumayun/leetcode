
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def lca(root, a, b):
    """
    Args:
     root(BinaryTreeNode_int32)
     a(BinaryTreeNode_int32)
     b(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    ans = []
    def build_path_to_node(root, node, curr):
        if root is None:
            return
        if root.value == node.value:
            curr.append(root.value)
            ans.append(curr[:])
            curr.pop()
            return

        curr.append(root.value)
        build_path_to_node(root.left, node, curr)
        curr.pop()

        curr.append(root.value)
        build_path_to_node(root.right, node, curr)
        curr.pop()

    build_path_to_node(root, a, [])
    build_path_to_node(root, b, [])
    set_a = set(ans[0])
    set_b = set(ans[1])
    return list(set_a.intersection(set_b))[-1]

if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    root.left.right.left = BinaryTreeNode(8)
    root.left.right.right = BinaryTreeNode(9)
    print(lca(root, root.left.left, root.left.right))
    print(lca(root, root.left.left, root.right.left))
    print(lca(root, root.left.left, root.right.right))