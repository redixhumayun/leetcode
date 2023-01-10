
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

def binary_tree_to_cdll(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    if root is None:
        return root

    def in_order_traversal(root):
        if root is None:
            return []
        return in_order_traversal(root.left) + [root.value] + in_order_traversal(root.right)
    
    in_order_list = in_order_traversal(root)

    head = BinaryTreeNode(in_order_list[0])
    prev = temp = head

    for index in range(1, len(in_order_list)):
        head.right = BinaryTreeNode(in_order_list[index])
        head = head.right
        head.left = prev
        prev = head

    head.right = temp
    temp.left = head

    return temp


if __name__ == '__main__':
    root = BinaryTreeNode(4)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(5)
    root.left.left = BinaryTreeNode(1)
    root.left.right = BinaryTreeNode(3)
    result = binary_tree_to_cdll(root)

    root = BinaryTreeNode(1)
    result = binary_tree_to_cdll(root)