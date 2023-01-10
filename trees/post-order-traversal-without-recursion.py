
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

def postorder_traversal_alternative(root):
    if root is None:
        return root
    
    result = []
    stack = []
    stack.append((root, "arrival"))
    while len(stack) > 0:
        (node, zone) = stack[-1]
        if zone == "arrival":
            stack[-1] = (node, "interim")
            if node.left:
                stack.append((node.left, "arrival"))
        elif zone == "interim":
            stack[-1] = (node, "departure")
            if node.right:
                stack.append((node.right, "arrival"))
        elif zone == "departure":
            result.append(node.value)
            stack.pop()
    return result

def postorder_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    if root is None:
        return root
    
    result = []
    stack = []
    stack.append((root, None))
    while len(stack) > 0:
        (node, zone) = stack[-1]
        if zone is None:
            stack[-1] = (node, "arrival")
            if node.left:
                stack.append((node.left, None))
        elif zone == "arrival":
            stack[-1] = (node, "interim")
            if node.right:
                stack.append((node.right, None))
        elif zone == "interim":
            stack[-1] = (node, "departure")
            result.append(node.value)
            stack.pop()
    return result

if __name__ == "__main__":
    root = BinaryTreeNode(100)
    root.left = BinaryTreeNode(200)
    root.right = BinaryTreeNode(300)
    root.left.left = BinaryTreeNode(400)
    root.left.right = BinaryTreeNode(500)
    print(postorder_traversal_alternative(root))