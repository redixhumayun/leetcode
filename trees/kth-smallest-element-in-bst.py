from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1 
        ans = None
        def recurse(root):
            nonlocal count, ans
            if root is None:
                return
            recurse(root.left)
            if count == k:
                ans = root.val
            count += 1
            recurse(root.right)
        recurse(root)
        return ans

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(Solution().kthSmallest(root, 1))
    # print(Solution().kthSmallest(root, 2))
    # print(Solution().kthSmallest(root, 3))
    # print(Solution().kthSmallest(root, 4))
    
    # root = TreeNode(5)
    # root.left = TreeNode(3)
    # root.right = TreeNode(6)
    # root.left.left = TreeNode(2)
    # root.left.right = TreeNode(4)
    # root.left.left.left = TreeNode(1)
    # print(Solution().kthSmallest(root, 3))