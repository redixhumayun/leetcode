class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder_iterative(root):
    stack = []
    preorder_list = []
    if root is None:
        return root

    stack.append(root)
    while len(stack) > 0:
        root = stack.pop()
        preorder_list.append(root.value)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return preorder_list

if __name__ == "__main__":
    root = BinaryTreeNode(2)
    root.left = BinaryTreeNode(5)
    root.right = BinaryTreeNode(4)
    root.left.left = BinaryTreeNode(0)
    root.left.right = BinaryTreeNode(1)
    root.right.left = BinaryTreeNode(3)
    root.right.right = BinaryTreeNode(6)
    print(preorder_iterative(root))