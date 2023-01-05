from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        max_value = TreeNode(float("inf"))
        def recurse(root):
            nonlocal max_value
            if root is None:
                return
            if p.val < root.val < max_value.val:
                max_value = root
            if p.val < root.val:
                recurse(root.left)
            else:
                recurse(root.right)
        recurse(root)
        if max_value.val == float("inf"):
            return None
        return max_value

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(Solution().inorderSuccessor(root, TreeNode(1)))