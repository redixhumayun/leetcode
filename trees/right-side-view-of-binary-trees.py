
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

    def print_tree(self):
        print(self.value)
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

from collections import deque

def right_view(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    queue = deque([root])
    output = []
    while len(queue) > 0:
        current_length = len(queue)
        for index in range(current_length):
            node = queue.popleft()
            if index == current_length - 1:
                output.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return output


if __name__ == "__main__":
    root = BinaryTreeNode(0)
    root.left = BinaryTreeNode(1)
    root.right = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(4)
    result = right_view(root)
    print(result)