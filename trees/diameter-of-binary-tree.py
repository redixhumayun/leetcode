
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

def binary_tree_diameter(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    if root is None:
        return 0

    ans = 0
    def recurse(root):
        nonlocal ans
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        left = recurse(root.left)
        right = recurse(root.right)
        ans = max(ans, left + right)
        return max(left, right) + 1

    result = recurse(root)
    return ans

if __name__ == "__main__":
    root = BinaryTreeNode(0)
    root.left = BinaryTreeNode(1)
    root.right = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(4)
    print(binary_tree_diameter(root))

    root = BinaryTreeNode(0)
    root.left = BinaryTreeNode(1)
    root.left.left = BinaryTreeNode(2)
    root.left.right = BinaryTreeNode(3)
    root.left.left.left = BinaryTreeNode(4)
    root.left.right.right = BinaryTreeNode(5)
    print(binary_tree_diameter(root))

    root = BinaryTreeNode(5)
    root.left = BinaryTreeNode(3)
    root.right = BinaryTreeNode(1)
    root.left.left = BinaryTreeNode(0)
    root.left.right = BinaryTreeNode(2)
    root.right.left = BinaryTreeNode(4)
    print(binary_tree_diameter(root))