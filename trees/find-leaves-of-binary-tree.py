# Definition for a binary tree node.

from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        hash_map = defaultdict(list)
        def recurse(root):
            if root is None:
                return 0
            left = recurse(root.left) + 1
            right = recurse(root.right) + 1
            index = max(left, right)
            hash_map[index].append(root.val)
            root.left = None
            root.right = None
            return left
        recurse(root)
        print(hash_map)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(Solution().findLeaves(root))