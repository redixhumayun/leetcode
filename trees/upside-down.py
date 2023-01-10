
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

def flip_upside_down(root) -> BinaryTreeNode | None:
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    root_flag = False
    new_root = None
    def recurse(root, parent):
        nonlocal root_flag, new_root
        if root is None:
            root_flag = True
            return
        recurse(root.left, root)
        root.right = parent
        if parent is not None:
            root.left = parent.right
        else:
            root.left = None
        if root_flag is True:
            new_root = root
            root_flag = False
        return
    recurse(root, None)
    return new_root


if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root: BinaryTreeNode | None = flip_upside_down(root)
    if root is not None:
        root.print_tree()

    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.left.left.left = BinaryTreeNode(6)
    root.left.left.right = BinaryTreeNode(7)
    root: BinaryTreeNode | None = flip_upside_down(root)
    if root is not None:
        root.print_tree()
    