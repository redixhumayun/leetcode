
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def print_tree(self, root):
        if root is None:
            return
        print(root.value)
        self.print_tree(root.left)
        self.print_tree(root.right)

def delete_from_bst(root: BinaryTreeNode, values_to_be_deleted) -> BinaryTreeNode:
    """
    Args:
     root(BinaryTreeNode_int32)
     values_to_be_deleted(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.

    #   This method will find the node to delete and its parent and return a tuple of both if found
    def find_node_in_bst(root, value, parent):
        if root is None:
            return (None, None)
        if root.value == value:
            return (root, parent)
        if value < root.value:
            return find_node_in_bst(root.left, value, root)
        else:
            return find_node_in_bst(root.right, value, root)

    def delete(root, value):
        node_to_delete, parent = find_node_in_bst(root, value, None)

        #   The node to delete cannot be found
        if node_to_delete is None:
            return root

        #   The node to delete is a leaf node
        if node_to_delete.left is None and node_to_delete.right is None:
            #   If the tree only has one node - the root node
            #   Just return a None value indicating an empty tree after deleting the root
            if parent is None:
                return None

            #   If the node is not the root node
            if parent.left is node_to_delete:
                parent.left = None
            elif parent.right is node_to_delete:
                parent.right = None
            return root

        #   The node to delete is either an internal node or a root node
        if node_to_delete.right is not None:
            #   Find the successor of the node
            successor_parent = node_to_delete
            successor = node_to_delete.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            node_to_delete.value = successor.value
            if successor is successor_parent.right:
                successor_parent.right = successor.right
            else:
                successor_parent.left = successor.right
            return root

        #   The node to delete is either an internal node or a root node but without a right child
        #   Find the predecessor and swap with that instead
        else:
            #   Find the predecessor of the node
            predecessor_parent = node_to_delete
            predecessor = node_to_delete.left
            while predecessor.right is not None:
                predecessor_parent = predecessor
                predecessor = predecessor.right

            node_to_delete.value = predecessor.value
            if predecessor is predecessor_parent.right:
                predecessor_parent.right = predecessor.left
            else:
                predecessor_parent.left = predecessor.left
            return root


        
    for value in values_to_be_deleted:
        root = delete(root, value)
    return root


if __name__ == '__main__':
    values = [5, 4]
    root = BinaryTreeNode(4)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(6)
    root.left.left = BinaryTreeNode(1)
    root.left.right = BinaryTreeNode(3)
    root.right.left = BinaryTreeNode(5)
    root.right.right = BinaryTreeNode(7)
    root: BinaryTreeNode = delete_from_bst(root, values)
    root.print_tree(root)