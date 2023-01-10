# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_list(self):
        print(self.val)
        if self.right:
            self.right.print_list()
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        
        def recurse(root):
            if root is None:
                return (None, None)
            #   Leaf node base case
            if not root.left and not root.right:
                return (root, root)

            (left_head, left_tail) = recurse(root.left)
            (right_head, right_tail) = recurse(root.right)
            head = root
            head.left = None

            if left_head is not None:
                head.right = left_head
                if right_head is not None:
                    left_tail.right = right_head
                    return (head, right_tail)
                else:
                    return (head, left_tail)
            
            if left_head is None and right_head is not None:
                head.right = right_head
                return (head, right_tail)

        (head, tail) = recurse(root)
        root = head
        root.print_list()
        
if __name__ == '__main__':
    sol = Solution()
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(5)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)
    # root.right.right = TreeNode(6)
    # sol.flatten(root)

    # root = TreeNode(0)
    # sol.flatten(root)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(5)
    sol.flatten(root)