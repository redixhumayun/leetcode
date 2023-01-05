from typing import Optional, List

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return ListNode()
        if list1 is None and list2 is not None:
            return list2
        if list1 is not None and list2 is None:
            return list1
        head1 = list1
        head2 = list2
        output_list = ListNode()
        temp = output_list
        while head1 and head2:
            val_1 = head1.val
            val_2 = head2.val
            if val_1 <= val_2:
                temp.next = ListNode()
                temp = temp.next
                temp.val = val_1
                head1 = head1.next
            else:
                temp.next = ListNode()
                temp = temp.next
                temp.val = val_2
                head2 = head2.next

        while head1:
            temp.next = ListNode()
            temp = temp.next
            temp.val = head1.val
            head1 = head1.next

        while head2:
            temp.next = ListNode()
            temp = temp.next
            temp.val = head2.val
            head2 = head2.next
        
        if output_list.next is not None:
            output_list = output_list.next
        output_list.print(output_list)
        return output_list

if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    print(Solution().mergeTwoLists(list1, list2))

    print(Solution().mergeTwoLists(ListNode(), ListNode()))

    print(Solution().mergeTwoLists(ListNode(), ListNode(0)))