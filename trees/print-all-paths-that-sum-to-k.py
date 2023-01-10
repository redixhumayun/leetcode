
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

def all_paths_sum_k(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
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
            if sum(curr) == k:
                ans.append(curr[:])
            curr.pop()
            return
        
        curr.append(root.value)
        recurse(root.left, curr)
        recurse(root.right, curr)
        curr.pop()

    recurse(root, [])
    if len(ans) == 0:
        ans.append([-1])
    return ans


if __name__ == '__main__':
    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(25)
    root.right = BinaryTreeNode(30)
    root.left.left = BinaryTreeNode(45)
    root.right.left = BinaryTreeNode(40)
    root.right.right = BinaryTreeNode(50)
    print(all_paths_sum_k(root, 80))