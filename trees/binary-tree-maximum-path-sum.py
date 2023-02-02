from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        def helper(node):
            nonlocal ans
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            ans = max(ans, node.val, node.val + left, node.val + right, node.val + left + right)
            return max(node.val, node.val + left, node.val + right)
        helper(root)
        return ans

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().maxPathSum(root))

    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().maxPathSum(root))

    root = TreeNode(2)
    root.left = TreeNode(-1)
    print(Solution().maxPathSum(root))

    root = TreeNode(0)
    root.left = TreeNode(0)
    print(Solution().maxPathSum(root))

    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)
    root.right.left.left = TreeNode(1)
    root.right.left.right = TreeNode(1)
    root.right.right.left = TreeNode(1)
    print(Solution().maxPathSum(root))