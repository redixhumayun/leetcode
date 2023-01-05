# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print("\n")
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        #   Find the left and right nodes that need to be reversed
        #   And the nodes one to the left of left and one to the right of right
        left_node = right_node = left_of_left = right_of_right = None
        head_sentinel = ListNode(None, head)
        temp = head_sentinel
        counter = 0
        while temp:
            if counter == left - 1:
                left_of_left = temp
            if counter == left:
                left_node = temp
            if counter == right:
                right_node = temp
            if counter == right + 1:
                right_of_right = temp
            temp = temp.next
            counter += 1
        
        prev = left_of_left
        curr = left_node
        number_of_iterations = right - left + 1
        while number_of_iterations > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            number_of_iterations -= 1
        
        left_of_left.next = prev
        left_node.next = right_of_right
        left_of_left.print(left_of_left)
        
if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(Solution().reverseBetween(head, 2, 4))