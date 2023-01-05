
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
        self.left: BinaryTreeNode | None = None
        self.right: BinaryTreeNode | None = None


def search_node_in_bst(root, value):
    """
    Args:
     root(BinaryTreeNode_int32)
     value(int32)
    Returns:
     bool
    """
    # Write your code here.
    if root is None:
        return False
    if root.value == value:
        return True
    if value < root.value:
        return search_node_in_bst(root.left, value)
    else:
        return search_node_in_bst(root.right, value)


if __name__ == '__main__':
    root = BinaryTreeNode(2)
    root.left = BinaryTreeNode(1)
    root.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(4)
    root.right.right = BinaryTreeNode(6)
    print(search_node_in_bst(root, 9))
    # print(search_node_in_bst(root, 3))
    # print(search_node_in_bst(root, 7))
    # print(search_node_in_bst(root, 2))
    # print(search_node_in_bst(root, 4))
    # print(search_node_in_bst(root, 6))
    # print(search_node_in_bst(root, 8))
    # print(search_node_in_bst(root, 1))
    # print(search_node_in_bst(root, 9))