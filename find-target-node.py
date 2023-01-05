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
    def tree_dfs(self, root, parent):
        if not root:
            return
        root.parent = parent
        self.tree_dfs(root.left, root)
        self.tree_dfs(root.right, root)

    def find_target_node(self, root, target):
        if not root:
            return None
        if root.val == target:
            return root
        return self.find_target_node(root.left, target) or self.find_target_node(root.right, target)

if __name__ == '__main__':
    root = TreeNode(8)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    root.right = TreeNode(1)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(9)

    Solution().tree_dfs(root, None)
    root.print(root)
    # print(Solution().find_target_node(root, 5).val)