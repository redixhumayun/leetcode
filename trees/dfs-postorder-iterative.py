class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder_iterative(root: BinaryTreeNode | None):
    if root is None:
        return root
    
    stack = []
    visited = set()
    post_order = []
    curr: BinaryTreeNode = root
    while len(stack) > 0 or curr is not None:
        if curr is not None:
            if curr in visited:
                post_order.append(curr.value)
                curr = None
            else:
                stack.append(curr)
                if curr.right:
                    stack.append(curr.right)
                visited.add(curr)
                curr = curr.left
        else:
            curr = stack.pop()
    return post_order

if __name__ == "__main__":
    root = BinaryTreeNode(2)
    root.left = BinaryTreeNode(5)
    root.right = BinaryTreeNode(4)
    root.left.left = BinaryTreeNode(0)
    root.left.right = BinaryTreeNode(1)
    root.right.left = BinaryTreeNode(3)
    root.right.right = BinaryTreeNode(6)
    print(postorder_iterative(root))