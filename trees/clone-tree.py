
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

    def print(self, root):
        if root is None:
            return
        print(root.value)
        self.print(root.left)
        self.print(root.right)

def clone_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    def clone_from_traversal(root):
        def in_order(root):
            if root is None:
                return []
            return in_order(root.left) + [root.value] + in_order(root.right)

        def pre_order(root):
            if root is None:
                return []
            return [root.value] + pre_order(root.left) + pre_order(root.right)

        pre_order_list = pre_order(root)
        in_order_list = in_order(root)

        def build_tree(pre_order_list, in_order_list):
            if not pre_order_list or not in_order_list:
                return None

            root = BinaryTreeNode(pre_order_list[0])
            mid = in_order_list.index(pre_order_list[0])
            root.left = build_tree(pre_order_list[1: mid + 1], in_order_list[:mid])
            root.right = build_tree(pre_order_list[mid+1 :], in_order_list[mid + 1:])
            return root

        return build_tree(pre_order_list, in_order_list)

    def recurse(root, clone_root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return BinaryTreeNode(root.value)
        clone_root = BinaryTreeNode(root.value)
        clone_root.left = recurse(root.left, clone_root.left)
        clone_root.right = recurse(root.right, clone_root.right)
        return clone_root

    return clone_from_traversal(root)
    # return recurse(root, None)


if __name__ == "__main__":
    root = BinaryTreeNode(100)
    root.left = BinaryTreeNode(200)
    root.right = BinaryTreeNode(300)
    root.left.left = BinaryTreeNode(400)
    root.left.right = BinaryTreeNode(500)
    # root.right.right = BinaryTreeNode(800)
    new_root = clone_tree(root)
    new_root.print(new_root)