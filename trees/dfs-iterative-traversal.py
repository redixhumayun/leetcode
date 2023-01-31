class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#   This solution is taken from here: https://uplevel.interviewkickstart.com/resource/editorial/rc-codingproblem-433360-792461-1042-6383
def iterative_traversal(root):
    if root is None:
        return []
    result = []
    stack = [(root, None)]
    while len(stack) > 0:
        (node, zone) = stack[-1]
        if zone is None:
            stack[-1] = (node, "arrival")
            result.append(node.value)
            if node.left is not None:
                stack.append((node.left, None))
        elif zone == "arrival":
            stack[-1] = (node, "interim")
            if node.right is not None:
                stack.append((node.right, None))
        elif zone == "interim":
            stack[-1] = (node, "departure")
            stack.pop()
    return result

if __name__ == "__main__":
    root = BinaryTreeNode(2)
    root.left = BinaryTreeNode(5)
    root.right = BinaryTreeNode(4)
    root.left.left = BinaryTreeNode(0)
    root.left.right = BinaryTreeNode(1)
    root.right.left = BinaryTreeNode(3)
    root.right.right = BinaryTreeNode(6)
    print(iterative_traversal(root))