
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next_right = None
"""
from collections import deque
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next_right = None
    
    def print(self, root):
        if root is None:
            return
        print(root.value)
        if root.next_right:
            print("Next right: ", root.next_right.value)
        else:
            print("Next right: ", root.next_right)
        self.print(root.left)
        self.print(root.right)

def populate_sibling_pointers(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    if root is None:
        return root
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        current_length = len(queue)
        for index in range(current_length):
            node = queue.popleft()
            if index == current_length - 1:
                node.next_right = None
            else:
                node.next_right = queue[0]

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return root


if __name__ == "__main__":
    root = BinaryTreeNode(100)
    root.left = BinaryTreeNode(200)
    root.right = BinaryTreeNode(300)
    root.left.left = BinaryTreeNode(400)
    root.left.right = BinaryTreeNode(500)
    root.right.left = BinaryTreeNode(600)
    root.right.right = BinaryTreeNode(700)
    root = populate_sibling_pointers(root)
    root.print(root)