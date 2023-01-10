
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

    def print(self):
        print(self.value)
        if self.left:
            self.left.print()
        if self.right:
            self.right.print()

def construct_binary_tree(inorder, preorder):
    """
    Args:
     inorder(list_int32)
     preorder(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    if len(preorder) == 0 or len(inorder) == 0:
        return None
    if len(inorder) == 1:
        #   Single node base case
        return BinaryTreeNode(inorder[0])

    root = BinaryTreeNode(preorder[0])
    inorder_index = inorder.index(root.value)
    root.left = construct_binary_tree(inorder[:inorder_index], preorder[1 : inorder_index + 1])
    root.right = construct_binary_tree(inorder[inorder_index + 1:], preorder[inorder_index + 1 : ])
    return root


if __name__ == '__main__':
    root = construct_binary_tree([3, 2, 1, 5, 4, 6], [1, 2, 3, 4, 5, 6])
    root.print()
    