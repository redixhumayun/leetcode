from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

    def print_tree(self, root):
        if root is None:
            return
        print(root.val)
        self.print_tree(root.left)
        self.print_tree(root.right)

class Solution:
    def findNodeParent(self, root: TreeNode | None, prev: TreeNode | None, key: int):
        if root is None:
            return None
        if root.val == key:
            return prev
        if root.val > key:
            return self.findNodeParent(root.left, root, key)
        else:
            return self.findNodeParent(root.right, root, key)

    def findNode(self, root: TreeNode | None, key: int):
        if root is None:
            return None
        if root.val == key:
            return root
        if root.val > key:
            return self.findNode(root.left, key)
        else:
            return self.findNode(root.right, key)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node_to_delete = self.findNode(root, key)
        node_to_delete_parent = self.findNodeParent(root, None, key)

        #   If the node to be deleted cannot be found, return the root of the tree
        if node_to_delete is None:
            return root

        #   If the node to delete is a leaf node, delete the parent's reference to the node
        if  node_to_delete.left is None and node_to_delete.right is None:
            #   The node to be removed is the root node, which is the only node in the tree
            if node_to_delete_parent is None:
                return None
            if node_to_delete_parent.val < node_to_delete.val:
                node_to_delete_parent.right = None
            else:
                node_to_delete_parent.left = None
            return root

        #   If the node to delete is not a leaf node
        elif node_to_delete is not None:
            #   If the node to be deleted has either a left child or a right child
            if node_to_delete.left is not None and node_to_delete.right is None:
                #   The node to be deleted has only a left child

                #   The node to be deleted is the root node
                if node_to_delete_parent is None:
                    return node_to_delete.left

                if node_to_delete_parent.val < node_to_delete.val:
                    node_to_delete_parent.right = node_to_delete.left
                else:
                    node_to_delete_parent.left = node_to_delete.left
                return root
            elif node_to_delete.left is None and node_to_delete.right is not None:
                #   The node to be deleted has only a right child

                #   The node to be deleted is the root node
                if node_to_delete_parent is None:
                    return node_to_delete.right

                if node_to_delete_parent.val < node_to_delete.val:
                    node_to_delete_parent.right = node_to_delete.right
                else:
                    node_to_delete_parent.left = node_to_delete.right
                return root

            #   If the node to be deleted has both a left child and a right child
            if node_to_delete.left is not None and node_to_delete.right is not None:
                #   Find the successor of the node to be deleted
                successor = node_to_delete.right
                prev = node_to_delete
                while successor.left is not None:
                    prev = successor
                    successor = successor.left
                
                #   Swap the node to be deleted with its successor
                node_to_delete.val = successor.val
                if prev.left is successor:
                    prev.left = successor.right
                else:
                    prev.right = successor.right
                return root


if __name__ == '__main__':
    # root = TreeNode(5)
    # root.left = TreeNode(3)
    # root.right = TreeNode(6)
    # root.left.left = TreeNode(2)
    # root.left.right = TreeNode(4)
    # root.right.right = TreeNode(7)
    # key = 5
    # solution = Solution()
    # r: TreeNode = solution.deleteNode(root, key)
    # r.print_tree(r)

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    key = 1
    solution = Solution()
    r: TreeNode = solution.deleteNode(root, key)
    r.print_tree(r)