
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
        
def path_sum(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     bool
    """
    # Write your code here.
    def recurse(root, sum):
        if not root.left and not root.right:
            sum += root.value
            if sum == k:
                return True
            return False
        sum += root.value
        left = right = False
        if root.left:
            left = recurse(root.left, sum)
        if root.right:
            right = recurse(root.right, sum)
        return left or right
    return recurse(root, 0)


if __name__ == "__main__":
    root = BinaryTreeNode(0)
    root.left = BinaryTreeNode(1)
    root.right = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(4)
    print(path_sum(root, 4))

    root = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.right.right = BinaryTreeNode(5)
    root.right.right.left = BinaryTreeNode(4)
    print(path_sum(root, 10))