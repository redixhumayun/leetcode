from typing import List, Optional

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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode:
        sum = 0
        carry = 0
        head = ListNode()
        result = head
        while l1 and l2:
            sum = l1.val + l2.val + carry
            digit = sum % 10
            carry = sum // 10
            result.val = digit
            if l1.next and l2.next:
                result.next = ListNode()
                result = result.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sum = l1.val + carry
            digit = sum % 10
            carry = sum // 10
            result.next = ListNode()
            result = result.next
            result.val = digit
            l1 = l1.next
        
        while l2:
            sum = l2.val + carry
            digit = sum % 10
            carry = sum // 10
            result.next = ListNode()
            result = result.next
            result.val = digit
            l2 = l2.next
        
        if carry != 0:
            result.next = ListNode()
            result = result.next
            result.val = carry

        return head

if __name__ == '__main__':
    linked_list_1 = ListNode(2, ListNode(4, ListNode(3)))
    linked_list_2 = ListNode(5, ListNode(6, ListNode(4)))
    result = Solution().addTwoNumbers(linked_list_1, linked_list_2)
    print(result.print(result))

    linked_list_1 = ListNode(0)
    linked_list_2 = ListNode(0)
    result = Solution().addTwoNumbers(linked_list_1, linked_list_2)
    print(result.print(result))

    linked_list_1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    linked_list_2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    result = Solution().addTwoNumbers(linked_list_1, linked_list_2)
    print(result.print(result))