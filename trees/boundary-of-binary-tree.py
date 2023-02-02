# Definition for a binary tree node.

from typing import Optional, List
from collections import deque, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        #   This is the iterative approach using a stack
        stack = []
        root_arr = [root.val]
        left_subtree_arr = []
        right_subtree_arr = []
        leaves_arr = []
        visited = set()
        visited.add(root)

        def is_leaf(node):
            return node.left is None and node.right is None
        
        node = root.left
        while node and not is_leaf(node):
            left_subtree_arr.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right

        node = root.right
        while node and not is_leaf(node):
            stack.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left

        def in_order_traversal(node):
            if node is None:
                return
            if is_leaf(node):
                if node not in visited:
                    leaves_arr.append(node.val)
                return
            in_order_traversal(node.left)
            in_order_traversal(node.right)

        in_order_traversal(root)
        while len(stack) > 0:
            value = stack.pop()
            right_subtree_arr.append(value)

        return root_arr + left_subtree_arr + leaves_arr + right_subtree_arr


        #   This is the DFS approach
        # root_arr = []
        # left_subtree_arr = []
        # right_subtree_arr = []
        # leaves_arr = []
        # def dfs_helper(node, parent, subtree):
        #     if node is None:
        #         return
        #     if node.left is None and node.right is None:
        #         leaves_arr.append(node.val)
        #         return
        #     #   If I am in the left subtree, check if I am the parents left child
        #     #   If I am, add to left boundary
        #     if subtree == "left":
        #         if node is parent.left:
        #             left_subtree_arr.append(node.val)
        #         elif parent.left is None:
        #             left_subtree_arr.append(node.val)

        #     #   Do opposite for the right
        #     if subtree == "right":
        #         if node is parent.right:
        #             right_subtree_arr.append(node.val)
        #         elif parent.right is None:
        #             right_subtree_arr.append(node.val)
            
        #     dfs_helper(node.left, node, subtree)
        #     dfs_helper(node.right, node, subtree)
        
        # root_arr.append(root.val)
        # dfs_helper(root.left, root, "left")
        # dfs_helper(root.right, root, "right")
        # right_subtree_arr.reverse()
        # return root_arr + left_subtree_arr + leaves_arr + right_subtree_arr
        #   This is the BFS approach
        # queue = deque([(root, None, 0)])
        # root_arr = []
        # left_subtree_arr = []
        # right_subtree_arr = []
        # leaves_arr = []

        # #   Handle root node
        # (current_node, subtree, level) = queue.popleft()
        # root_arr.append(current_node.val)
        # if current_node.left:
        #     queue.append((current_node.left, "left", level - 1))
        # if current_node.right:
        #     queue.append((current_node.right, "right", level - 1))

        # while len(queue) > 0:
        #     current_length = len(queue)
        #     for index in range(current_length):
        #         (current_node, subtree, level) = queue.popleft()
                
        #         if current_node.left:
        #             queue.append((current_node.left, subtree, level - 1))
        #         if current_node.right:
        #             queue.append((current_node.right, subtree, level - 1))

        #         if current_node.left is None and current_node.right is None:
        #             leaves_arr.append((current_node.val, level))
        #         else:
        #             if subtree == "left":
        #                 if index == 0:
        #                     left_subtree_arr.append(current_node.val)
        #             if subtree == "right":
        #                 if index == current_length - 1:
        #                     right_subtree_arr.append(current_node.val)

        # right_subtree_arr.reverse()
        # leaves_arr.sort(key=lambda x:x[1])
        # leaves_arr = [current_node for (current_node, level) in leaves_arr]
        # return root_arr + left_subtree_arr + leaves_arr + right_subtree_arr

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    print(Solution().boundaryOfBinaryTree(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.left.left = TreeNode(9)
    root.right.left.right = TreeNode(10)
    print(Solution().boundaryOfBinaryTree(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(4)
    print(Solution().boundaryOfBinaryTree(root))