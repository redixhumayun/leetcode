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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        array = []
        for list in lists:
            head = list
            while head is not None:
                array.append(head.val)
                head = head.next
        
        if len(array) == 0:
            return None

        array.sort()
        new_list_head = ListNode()
        temp = new_list_head
        for num in array:
            temp.next = ListNode()
            temp = temp.next
            temp.val = num
        
        if new_list_head.next is not None:
            new_list_head = new_list_head.next
        # new_list_head.print(new_list_head)
        return new_list_head

if __name__ == "__main__":
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))
    # print(Solution().mergeKLists([list1, list2, list3]))

    print(Solution().mergeKLists([]))

    list1 = ListNode(0, None)
    print(Solution().mergeKLists([list1]))