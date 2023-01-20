from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print(self):
        print(self.val)
        if self.left is not None:
            self.left.print()
        if self.right is not None:
            self.right.print()

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root, level):
            if root is None:
                return None
            if root.left is None and root.right is None:
                return root
            #   Swap the children of all the even levels
            if level % 2 == 0:
                temp = root.left.val
                root.left.val = root.right.val
                root.right.val = temp
            root.left = helper(root.left, level + 1)
            root.right = helper(root.right, level + 1)
            return root
        return helper(root, 0)


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(13)
    root.right.left = TreeNode(21)
    root.right.right = TreeNode(34)
    print(Solution().reverseOddLevels(root))
    root.print()