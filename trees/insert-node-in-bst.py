
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

def build_a_bst(values):
    """
    Args:
     values(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    def insert(root, value):
        if root is None:
            root = BinaryTreeNode(value)
            return root
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
        return root
    root = BinaryTreeNode(values[0])
    for index in range(1, len(values)):
        insert(root, values[index])
    return root


if __name__ == '__main__':
    values = [7, 5, 9]
    root = build_a_bst(values)
    print(root.value)
    print(root.left.value)
    print(root.right.value)