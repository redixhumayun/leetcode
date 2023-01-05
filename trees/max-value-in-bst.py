
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

def get_maximum_value(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    def recurse(root):
        if root.right is None:
            return root.value
        return recurse(root.right)
    return recurse(root)


if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(4)
    root.right.right = BinaryTreeNode(6)
    print(get_maximum_value(root))