
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

def find_largest_bst(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    def is_valid_bst(root, left_bound, right_bound):
        if root is None:
            return True

        if not (left_bound < root.value < right_bound):
            return False

        left_result = is_valid_bst(root.left, left_bound, root.value)
        right_result = is_valid_bst(root.right, root.value, right_bound)
        return left_result and right_result

    def get_count_of_current_tree(root):
        if root is None:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + get_count_of_current_tree(root.left) + get_count_of_current_tree(root.right)

    max_count = 0
    def post_order_traversal(root):
        nonlocal max_count
        if root is None:
            return
            
        left_subtree = post_order_traversal(root.left)
        right_subtree = post_order_traversal(root.right)

        #   If either of the two subtrees is not a valid BST, don't check
        if left_subtree is False or right_subtree is False:
            return

        if left_subtree is True and right_subtree is True:
            left_value = 10**10
            if root.left:
                left_value = root.left.value

            right_value = 10**10
            if root.right:
                right_value = root.right.value

            if left_value <= root.value <= right_value:
                count = get_count_of_current_tree(root)
                max_count = max(max_count, count)
                return True

        if is_valid_bst(root, float("-inf"), float("inf")):
            count = get_count_of_current_tree(root)
            max_count = max(max_count, count)
            return True
        return False
    
    post_order_traversal(root)
    return max_count


if __name__ == "__main__":
    root = BinaryTreeNode(100)
    root.left = BinaryTreeNode(300)
    root.right = BinaryTreeNode(500)
    root.left.left = BinaryTreeNode(200)
    root.left.right = BinaryTreeNode(400)
    root.right.left = BinaryTreeNode(600)
    root.right.right = BinaryTreeNode(700)
    print(find_largest_bst(root))

    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(20)
    root.right = BinaryTreeNode(30)
    print(find_largest_bst(root))