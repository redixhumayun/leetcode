
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

    def print_tree(self):
        print(self.value)
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

def merge_two_binary_search_trees(root1, root2):
    """
    Args:
     root1(BinaryTreeNode_int32)
     root2(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    if root1 is None and root2 is not None:
        return root2
    elif root1 is not None and root2 is None:
        return root1
    elif root1 is None and root2 is None:
        return None

    def in_order_list_constructor(root):
        if root is None:
            return []
        return in_order_list_constructor(root.left) + [root.value] + in_order_list_constructor(root.right)
    
    def construct_tree(node_list):
        if len(node_list) == 2:
            root = BinaryTreeNode(node_list[0])
            root.right = BinaryTreeNode(node_list[1])
            return root
        if len(node_list) == 1:
            root = BinaryTreeNode(node_list[0])
            return root

        mid_index = len(node_list) // 2
        root = BinaryTreeNode(node_list[mid_index])
        root.left = construct_tree(node_list[:mid_index])
        root.right = construct_tree(node_list[mid_index + 1:])
        return root


    in_order_list_1 = in_order_list_constructor(root1)
    in_order_list_2 = in_order_list_constructor(root2)
    in_order_list = in_order_list_1 + in_order_list_2
    in_order_list.sort()
    return construct_tree(in_order_list)

if __name__ == "__main__":
    root1 = BinaryTreeNode(2)
    root1.left = BinaryTreeNode(1)
    root1.right = BinaryTreeNode(2)

    root2 = BinaryTreeNode(3)
    root2.left = BinaryTreeNode(3)

    root = merge_two_binary_search_trees(root1, root2)
    root.print_tree()

    root1 = BinaryTreeNode(5)
    root1.left = BinaryTreeNode(3)
    root1.right = BinaryTreeNode(6)
    root1.left.left = BinaryTreeNode(2)
    root1.left.right = BinaryTreeNode(4)
    root1.right.right = BinaryTreeNode(7)

    root2 = BinaryTreeNode(8)
    root2.left = BinaryTreeNode(1)
    root2.right = BinaryTreeNode(9)

    root = merge_two_binary_search_trees(root1, root2)
    root.print_tree()
