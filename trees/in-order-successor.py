from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.successor = None
        self.previous = None

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        max_value = TreeNode(float("inf"))
        def recurse(root):
            nonlocal max_value
            if root is None:
                return
            if p.val < root.val < max_value.val:
                max_value = root
            if p.val < root.val:
                recurse(root.left)
            else:
                recurse(root.right)
        recurse(root)
        if max_value.val == float("inf"):
            return None
        return max_value

    """
    This method is taken from the leetcode solution: https://leetcode.com/problems/inorder-successor-in-bst/solutions/1104016/inorder-successor-in-bst/
    It involves handling two cases
    1. When the node whose successor needs to be found has a right child - in this case, find the minimum element in the right subtree of the node
    2. When the node does not have a right child - in this case, the in-order successor of the node can be found by performing
    an in-order traversal
    This solution works for any binary tree, not just a balanced binary search tree
    """
    def inorderSuccessorTraversal(self, root: TreeNode, previous: TreeNode | None, p: TreeNode):
        if root is None:
            return
        self.inorderSuccessorTraversal(root.left, root, p)
        if self.previous is p:
            self.successor = root
            return
        self.previous = root
        self.inorderSuccessorTraversal(root.right, root, p)

    def inorderSuccessorLeetcodeSolution(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        #   Case 1
        if p.right is not None:
            successor = p.right
            while successor.left is not None:
                successor = successor.left
            return successor

        #   Case 2
        else:
            self.inorderSuccessorTraversal(root, None, p)
            return self.successor

if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(4)
    root.right = TreeNode(10)
    root.left.left = TreeNode(2)
    root.right.left = TreeNode(8)
    root.right.right = TreeNode(12)
    root.left.left.right = TreeNode(3)
    result = Solution().inorderSuccessorLeetcodeSolution(root, root.right.left)
    print(result.val)