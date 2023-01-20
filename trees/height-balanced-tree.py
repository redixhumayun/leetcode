from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 1
            left_subtree_length = helper(root.left)
            right_subtree_length = helper(root.right)
            if abs(left_subtree_length - right_subtree_length) > 1:
                self.result = False
            return 1 + max(left_subtree_length, right_subtree_length)
        helper(root)
        return self.result

if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    print(Solution().isBalanced(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.right.right = TreeNode(4)
    print(Solution().isBalanced(root))
    