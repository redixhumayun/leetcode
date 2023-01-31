
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
class BinaryTreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def helper(node):
            if node is None:
                return (None, None)
            #   Leaf node
            if node.left is None and node.right is None:
                return (node, None)
            
            #   Internal node
            (left_head, left_tail) = helper(node.left)
            (right_head, right_tail) = helper(node.right)

            if left_head is None and left_tail is None:
                left_head = node
            elif left_tail is None:
                left_head.right = node
                node.left = left_head
            else:
                left_tail.right = node
                node.left = left_tail

            if right_head is None and right_tail is None:
                right_head = node
            else:
                node.right = right_head
                right_head.left = node

            if left_tail is None or right_tail is None:
                return (left_head, right_head)
            return (left_head, right_tail)
        
        (head, tail) = helper(root)
        if head is None:
            return None
        if tail is None:
            head.left = head
            head.right = head
            return head
        head.left = tail
        tail.right = head
        return head

# def binary_tree_to_cdll(root):
#     """
#     Args:
#      root(BinaryTreeNode_int32)
#     Returns:
#      BinaryTreeNode_int32
#     """
#     # Write your code here.

#     #   This is the in place solution that runs in O(N) time
#     def helper(node):
#         if node is None:
#             return (None, None)
#         #   leaf node
#         if node.left is None and node.right is None:
#             head = LinkedListNode(node.val)
#             return (head, None)
#         #   internal node
#         (left_head, left_tail) = helper(node.left)
#         (right_head, right_tail) = helper(node.right)
#         ll_node = LinkedListNode(node.val)
#         if left_tail is None:
#             left_head.next = ll_node
#             ll_node.prev = left_head
#         else:
#             left_tail.next = ll_node
#             ll_node.prev = left_tail
        
#         ll_node.next = right_head
#         right_head.prev = ll_node
#         if left_tail is None or right_tail is None:
#             return (left_head, right_head)
#         return (left_head, right_tail)

#     (head, tail) = helper(root)
#     head.prev = tail
#     tail.next = head

#     return head


    #   This is the solution that uses O(N) additional space by converting the nodes 
    # if root is None:
    #     return root

    # def in_order_traversal(root):
    #     if root is None:
    #         return []
    #     return in_order_traversal(root.left) + [root.value] + in_order_traversal(root.right)
    
    # in_order_list = in_order_traversal(root)

    # head = BinaryTreeNode(in_order_list[0])
    # prev = temp = head

    # for index in range(1, len(in_order_list)):
    #     head.right = BinaryTreeNode(in_order_list[index])
    #     head = head.right
    #     head.left = prev
    #     prev = head

    # head.right = temp
    # temp.left = head

    # return temp


if __name__ == '__main__':
    root = BinaryTreeNode(4)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(5)
    root.left.left = BinaryTreeNode(1)
    root.left.right = BinaryTreeNode(3)
    # result = binary_tree_to_cdll(root)
    result = Solution().treeToDoublyList(root)
    print(result)
    
    root = BinaryTreeNode(2)
    root.left = BinaryTreeNode(1)
    root.right = BinaryTreeNode(3)
    result = Solution().treeToDoublyList(root)
    print(result)

    root = BinaryTreeNode(1)
    result = Solution().treeToDoublyList(root)
    print(result)

    root = BinaryTreeNode(2)
    root.right = BinaryTreeNode(1)
    result = Solution().treeToDoublyList(root)
    print(result)

    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    result = Solution().treeToDoublyList(root)
    print(result)

    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(-1)
    root.right = BinaryTreeNode(9)
    result = Solution().treeToDoublyList(root)
    print(result)