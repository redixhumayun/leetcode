class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def print(self, root):
        if root:
            print(root.val)
            self.print(root.left)
            self.print(root.right)

class Solution:
    def recurse(self, root, target):
        if not root:
            print("Returning dict")
            return { 'difference': float("inf"), 'value': None }
        if target < root.val:
            left = self.closestValue(root.left, target)
            diff = abs(root.val - target)
            if diff < left['difference']:
                return { 'difference': diff, 'value': root.val }
            else:
                return { 'difference': left['difference'], 'value': root.left.val }
        else:
            print(root.val)
            right = self.closestValue(root.right, target)
            diff = abs(root.val - target)
            if diff < right['difference']:
                return { 'difference': diff, 'value': root.val }
            else:
                return { 'difference': right['difference'], 'value': root.right.val }
    def closestValue(self, root, target: float) -> int:
        ans = self.recurse(root, target)
        return ans['value']

if __name__ == '__main__':
    root = TreeNode(8)
    root.left = TreeNode(1)
    root.print(root)

    print(Solution().closestValue(root, 4.428571))