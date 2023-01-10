
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

def preorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    def recurse(root):
        if root is None:
            return []
        return [root.value] + recurse(root.left) + recurse(root.right)
    return recurse(root)


if __name__ == "__main__":
    root = BinaryTreeNode(2)
    root.left = BinaryTreeNode(5)
    root.right = BinaryTreeNode(4)
    root.left.left = BinaryTreeNode(0)
    root.left.right = BinaryTreeNode(1)
    root.right.left = BinaryTreeNode(3)
    root.right.right = BinaryTreeNode(6)
    print(preorder(root))