
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

def is_bst(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """
    # Write your code here.
    def recurse(root, small, large):
        if root is None:
            return True

        if root.value > large or root.value < small:
            return False

        left = recurse(root.left, small, root.value)
        right = recurse(root.right, root.value, large)

        return left and right

    return recurse(root, float("-inf"), float("inf"))


    #   This approach constructs an in-order traversal of the binary search tree and checks if the list
    #   is sorted
    # def in_order_traversal(root):
    #     if root is None:
    #         return []
    #     return in_order_traversal(root.left) + [root.value] + in_order_traversal(root.right)
    # in_order_list = in_order_traversal(root)

    # #   Check if the list is sorted
    # for index in range(len(in_order_list) - 1):
    #     if in_order_list[index] > in_order_list[index + 1]:
    #         return False
    # return True      


if __name__ == "__main__":
    root = BinaryTreeNode(30)
    root.left = BinaryTreeNode(5)
    root.right = BinaryTreeNode(40)
    root.right.left = BinaryTreeNode(10)
    root.right.right = BinaryTreeNode(50)
    print(is_bst(root))