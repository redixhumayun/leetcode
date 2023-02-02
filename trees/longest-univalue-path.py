# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_length = float("-inf")
        def helper(node):
            nonlocal max_length
            if node is None:
                return (True, 0, None)
            if node.left is None and node.right is None:
                new_length = 0
                max_length = max(new_length, max_length)
                return (True, 0, node.val)

            (is_left_univalue, left_length, left_root_value) = helper(node.left)
            (is_right_univalue, right_length, right_root_value) = helper(node.right)

            left_path = right_path = 0
            if is_left_univalue is True and node.val == left_root_value:
                left_path = left_length + 1
            if is_right_univalue is True and node.val == right_root_value:
                right_path = right_length + 1

            max_length = max(max_length, left_path + right_path)

            if is_left_univalue is True and node.val == left_root_value:
                return (True, max(left_path, right_path), node.val)

            if is_right_univalue is True and node.val == right_root_value:
                return (True, max(left_path, right_path), node.val)

            return (False, 0, node.val)


        helper(root)
        return max_length

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(5)
    print(Solution().longestUnivaluePath(root))

    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)
    print(Solution().longestUnivaluePath(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(3)
    print(Solution().longestUnivaluePath(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    print(Solution().longestUnivaluePath(root))

    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)
    root.right.left.left = TreeNode(1)
    root.right.left.right = TreeNode(1)
    root.right.right.left = TreeNode(1)
    print(Solution().longestUnivaluePath(root))