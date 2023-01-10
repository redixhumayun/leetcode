
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

class TreeIterator:
    def __init__(self, root):
        self.root = root
        self.previous_node_returned = None
        self.stack = [(self.root, "arrival")]

    def has_next(self):
        while len(self.stack) > 0:
            (node, zone) = self.stack[-1]
            if zone == "departure":
                self.stack.pop()
            else:
                break
        if len(self.stack) > 0:
            return 1
        return 0

    def next(self):
        while len(self.stack) > 0:
            (node, zone) = self.stack[-1]
            if zone == "arrival":
                self.stack[-1] = (node, "interim")
                if node.left:
                    self.stack.append((node.left, "arrival"))
            elif zone == "interim":
                self.stack[-1] = (node, "departure")
                return node
            elif zone == "departure":
                self.stack.pop()
        

def implement_tree_iterator(root, operations):
    """
    Args:
     root(BinaryTreeNode_int32)
     operations(list_str)
    Returns:
     list_int32
    """
    # Write your code here.
    iterator = TreeIterator(root)
    output = []
    for operation in operations:
        if operation == "next":
            result = iterator.next()
            if result is not None:
                if result.right:
                    iterator.stack.append((result.right, "arrival"))
                output.append(result.value)
            else:
                output.append(0)
        else:
            result = iterator.has_next()
            output.append(result)
    return output


if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    root.left.right.left = BinaryTreeNode(8)
    root.left.right.right = BinaryTreeNode(9)
    operations = ["next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    # print(implement_tree_iterator(root, operations))

    root = BinaryTreeNode(200)
    root.left = BinaryTreeNode(100)
    root.right = BinaryTreeNode(300)
    operations = ["next", "has_next", "next", "next", "has_next", "has_next", "next"]
    print(implement_tree_iterator(root, operations))