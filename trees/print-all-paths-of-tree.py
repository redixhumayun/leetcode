
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

def all_paths_of_a_binary_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    ans = []
    def recurse(root, curr):
        if root is None:
            return

        if root.left is None and root.right is None:
            curr.append(root.value)
            ans.append(curr[:])
            curr.pop()
            return
        
        curr.append(root.value)
        recurse(root.left, curr)
        curr.pop()

        curr.append(root.value)
        recurse(root.right, curr)
        curr.pop()
        
    recurse(root, [])
    return ans


if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    print(all_paths_of_a_binary_tree(root))

    root = BinaryTreeNode(100)
    root.left = None
    root.right = BinaryTreeNode(200)
    print(all_paths_of_a_binary_tree(root))