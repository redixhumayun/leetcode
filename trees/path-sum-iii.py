from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def check_sums(arr):
            count = 0
            sum_so_far = 0
            for i in range(len(arr)):
                for j in range(i, len(arr)):
                    sum_so_far += arr[j]
                    if sum_so_far > targetSum:
                        sum_so_far = 0
                        break
                    if sum_so_far == targetSum:
                        count += 1
            return count

        path_count = 0
        def helper(root, curr):
            nonlocal path_count
            if root is None:
                return
            if root.left is None and root.right is None:
                curr.append(root.val)
                count_sum = check_sums(curr)
                path_count += count_sum
                curr.pop()
            curr.append(root.val)
            helper(root.left, curr)
            helper(root.right, curr)
            curr.pop()
        helper(root, [])
        return path_count


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)
    print(Solution().pathSum(root, 8))
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # print(Solution().pathSum(root, 3))
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    # print(Solution().pathSum(root, 10))