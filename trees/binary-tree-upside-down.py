# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_tree(self):
        print(self.val)
        if self.left is not None:
            self.left.print_tree()
        if self.right is not None:
            self.right.print_tree()
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.left is None and root.right is None:
            return root

        new_root = None
        def helper(node, parent):
            nonlocal new_root
            if node is None:
                return None
            if node.left is None and node.right is None:
                node.right = parent
                node.left = parent.right
                if new_root is None:
                    new_root = node
                return node
            helper(node.left, node)
            if parent is None:
                node.left = None
            else:
                node.left = parent.right
            node.right = parent
            return node
        helper(root, None)
        return new_root

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    new_root = Solution().upsideDownBinaryTree(root)
    new_root.print_tree()

    root = TreeNode(2)
    new_root = Solution().upsideDownBinaryTree(root)
    new_root.print_tree()