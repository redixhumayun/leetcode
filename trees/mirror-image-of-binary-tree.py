
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

def mirror_image(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     Nothing
    """
    # Write your code here.
    def recurse(root):
        if root is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        recurse(root.left)
        recurse(root.right)

    recurse(root)


if __name__ == "__main__":
    root = BinaryTreeNode(0)
    root.left = BinaryTreeNode(1)
    root.right = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(4)
    root.right.left = BinaryTreeNode(5)
    root.right.right = BinaryTreeNode(6)
    mirror_image(root)
    root.print(root)