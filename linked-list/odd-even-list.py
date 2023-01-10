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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None


        temp_head = head

        #   Create the odd list
        odd_list = ListNode(-10**7)
        temp_odd_head = odd_list
        while temp_head:
            temp_odd_head.val = temp_head.val
            if temp_head.next:
                temp_odd_head.next = ListNode(-10**7)
                temp_odd_head = temp_odd_head.next
                temp_head = temp_head.next.next
            else:
                temp_head = None

        #   Create the even list
        temp_head = head
        temp_head = temp_head.next

        even_list = ListNode(-10**7)
        temp_even_head = even_list
        while temp_head:
            temp_even_head.val = temp_head.val
            if temp_head.next:
                temp_even_head.next = ListNode(-10**7)
                temp_even_head = temp_even_head.next
                temp_head = temp_head.next.next
            else:
                temp_head = None

        if even_list.val == -10**7:
            even_list = None

        if even_list is None:
            return odd_list

        ret_list = ListNode()
        temp_ret_list = ret_list

        while odd_list:
            temp_ret_list.val = odd_list.val
            if odd_list.next and odd_list.next.val != -10**7:
                temp_ret_list.next = ListNode()
                temp_ret_list = temp_ret_list.next
                odd_list = odd_list.next
            else:
                break

        temp_ret_list.next = ListNode()
        temp_ret_list = temp_ret_list.next
        while even_list:
            temp_ret_list.val = even_list.val
            if even_list.next and even_list.next.val != -10**7:
                temp_ret_list.next = ListNode()
                temp_ret_list = temp_ret_list.next
                even_list = even_list.next
            else:
                break

        return ret_list
        


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ret_list = Solution().oddEvenList(head)
    ret_list.print()

    head = ListNode(1)
    ret_list = Solution().oddEvenList(head)
    ret_list.print()