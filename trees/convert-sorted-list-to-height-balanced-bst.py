
"""
For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def print(self):
        print(self.value)
        if self.left:
            self.left.print()
        if self.right:
            self.right.print()

def sorted_list_to_bst(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    if head is None:
        return head

    if head.next is None:
        return BinaryTreeNode(head.value)

    def find_mid_of_list(list_head):
        slow = fast = list_head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev is not None:
            prev.next = None

        return slow
        

    def construct_tree(list_head):
        if list_head is None:
            return None

        #   Single node list
        if list_head.next is None:
            return BinaryTreeNode(list_head.value)

        mid = find_mid_of_list(list_head)
        first_head = list_head
        second_head = mid.next

        left = construct_tree(first_head)
        right = construct_tree(second_head)

        root = BinaryTreeNode(mid.value)
        root.left = left
        root.right = right

        return root
    
    return construct_tree(head)


if __name__ == "__main__":
    head = LinkedListNode(-1)
    head.next = LinkedListNode(2)
    head.next.next = LinkedListNode(3)
    head.next.next.next = LinkedListNode(5)
    head.next.next.next.next = LinkedListNode(6)
    head.next.next.next.next.next = LinkedListNode(7)
    head.next.next.next.next.next.next = LinkedListNode(10)
    root = sorted_list_to_bst(head)
    root.print()

    head = None
    root = sorted_list_to_bst(head)
    print(root)

    head = LinkedListNode(1)
    root = sorted_list_to_bst(head)
    root.print()