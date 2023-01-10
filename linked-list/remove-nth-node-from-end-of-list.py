# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        print(self.val)
        if self.next:
            self.next.print()

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast_pointer = slow_pointer = head
        prev_slow_pointer = None
        counter = n - 1
        while counter > 0:
            counter -= 1
            fast_pointer = fast_pointer.next

        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next
            prev_slow_pointer = slow_pointer
            slow_pointer = slow_pointer.next

        
        #   If the node to remove is the head
        if prev_slow_pointer is None:
            return slow_pointer.next
        #   If the node to remove is the last one
        if slow_pointer is fast_pointer:
            prev_slow_pointer.next = None
            return head

        #   If the node to remove is an internal node
        prev_slow_pointer.next = slow_pointer.next
        return head

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    result = Solution().removeNthFromEnd(head, n)
    result.print()

    head = ListNode(1)
    n = 1
    result = Solution().removeNthFromEnd(head, n)
    if result is not None:
        result.print()
    else:
        print(None)

    head = ListNode(1, ListNode(2))
    n = 1
    result = Solution().removeNthFromEnd(head, n)
    result.print()

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
    n = 7
    result = Solution().removeNthFromEnd(head, n)
    result.print()