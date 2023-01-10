
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

from collections import deque

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    queue = deque([root])
    output = []
    while queue:
        current_length = len(queue)
        level = []
        for _ in range(current_length):
            node = queue.popleft()
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        output.append(level)
    return output


if __name__ == "__main__":
    root = BinaryTreeNode(2)
    root.left = BinaryTreeNode(5)
    root.right = BinaryTreeNode(4)
    root.left.left = BinaryTreeNode(0)
    root.left.right = BinaryTreeNode(1)
    root.right.left = BinaryTreeNode(3)
    root.right.right = BinaryTreeNode(6)
    print(level_order_traversal(root))