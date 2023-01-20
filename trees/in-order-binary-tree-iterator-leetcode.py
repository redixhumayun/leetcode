# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = [(self.root, "arrival")]
        

    def next(self) -> int:
        if self.root is None:
            return -1
        
        while len(self.stack) > 0:
            (node, zone) = self.stack[-1]
            if zone == "arrival":
                self.stack[-1] = (node, "interim")
                if node.left is not None:
                    self.stack.append((node.left, "arrival"))

            if zone == "interim":
                self.stack[-1] = (node, "departure")
                if node.right is not None:
                    self.stack.append((node.right, "arrival"))
                return node.val

            if zone == "departure":
                self.stack.pop()

    def hasNext(self) -> bool:
        while len(self.stack) > 0 and self.stack[-1][1] == "departure":
            self.stack.pop()
        if len(self.stack) > 0:
            return True
        return False
        
if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    iterator = BSTIterator(root)
    print(iterator.next())
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()