# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        sum_value = 0
        def helper(root):
            nonlocal sum_value
            if root is None:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            tilt_value = abs(left - right)
            sum_value += tilt_value
            return left + root.val + right
        helper(root)
        return sum_value

    
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().findTilt(root))
    
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(9)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)
    print(Solution().findTilt(root))