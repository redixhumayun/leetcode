class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_iterative(root):
    stack = []
    inorder_list = []
    if root is None:
        return root
    
    node = root
    while True:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            if len(stack) == 0:
                break
            node = stack.pop()
            inorder_list.append(node.value)
            node = node.right
    return inorder_list

if __name__ == "__main__":
    root = BinaryTreeNode(2)
    root.left = BinaryTreeNode(5)
    root.right = BinaryTreeNode(4)
    root.left.left = BinaryTreeNode(0)
    root.left.right = BinaryTreeNode(1)
    root.right.left = BinaryTreeNode(3)
    root.right.right = BinaryTreeNode(6)
    print(inorder_iterative(root))