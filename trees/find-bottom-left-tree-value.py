# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        min_level = float("inf")
        ans = None
        def helper(root, level):
            nonlocal min_level, ans
            if root is None:
                return
            if level < min_level and root.left is None and root.right is None:
                min_level = level
                ans = root.val
            helper(root.left, level - 1)
            helper(root.right, level - 1)
        helper(root, 0)
        return ans

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(Solution().findBottomLeftValue(root))
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    print(Solution().findBottomLeftValue(root))
    
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.right = TreeNode(4)
    # root.right.left = TreeNode(5)
    # root.right.right = TreeNode(6)
    # root.right.left.left = TreeNode(7)
    # print(Solution().findBottomLeftValue(root))