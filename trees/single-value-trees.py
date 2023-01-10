
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

def find_single_value_trees(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    count = 0
    def helper(root):
        nonlocal count
        if root is None:
            return True

        #   Every leaf node is a unival tree
        if not root.left and not root.right:
            count += 1
            return True

        left = helper(root.left)
        right = helper(root.right)

        #   if either of the subtrees is not unival, current tree cannot be unival
        if left is False or right is False:
            return False

        left_tree = right_tree = False

        #   If left subtree is null, it is a unival tree
        if not root.left:
            left_tree = True
        else:
            if root.value == root.left.value:
                left_tree = True

        if not root.right:
            right_tree = True
        else:
            if root.value == root.right.value:
                right_tree = True
        
        if left_tree is True and right_tree is True:
            count += 1
            return True
        return False

    if not root:
        return 0

    helper(root)

    return count


if __name__ == '__main__':
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(1)
    root.right = BinaryTreeNode(1)
    root.left.left = BinaryTreeNode(1)
    root.left.right = BinaryTreeNode(1)
    root.right.left = BinaryTreeNode(2)
    root.right.right = BinaryTreeNode(1)
    print(find_single_value_trees(root))