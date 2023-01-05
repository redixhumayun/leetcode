from typing import Optional

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
    def find_mid(self, head) -> ListNode:
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev is not None:
            prev.next = None
        return slow

    def mergeLists(self, left, right):
        output_list = ListNode()
        temp = output_list
        while left and right:
            if left.val <= right.val:
                temp.next = ListNode()
                temp = temp.next
                temp.val = left.val
                left = left.next
            else:
                temp.next = ListNode()
                temp = temp.next
                temp.val = right.val
                right = right.next

        while left:
            temp.next = ListNode()
            temp = temp.next
            temp.val = left.val
            left = left.next

        while right:
            temp.next = ListNode()
            temp = temp.next
            temp.val = right.val
            right = right.next

        if output_list.next is not None:
            output_list = output_list.next

        return output_list

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #   This approach uses merge sort on a linked list
        #   Base cases
        if head is None:
            return
        if head is not None and head.next is None:
            #   Single node here
            return head

        mid = self.find_mid(head)
        first_head = head
        second_head = mid

        #   The first list is from head to mid
        #   The second list is from mid.next to tail
        left_sorted = self.sortList(first_head)
        right_sorted = self.sortList(second_head)

        return self.mergeLists(left_sorted, right_sorted)

        #   This approach converts list to array, sorts it and then re-converts to list
        # if head is None:
        #     return None
        # array = []
        # while head:
        #     array.append(head.val)
        #     head = head.next
        
        # array.sort()
        # print(array)

        # return_list = ListNode()
        # temp = return_list
        # for num in array:
        #     temp.next = ListNode()
        #     temp = temp.next
        #     temp.val = num

        # if return_list.next is not None:
        #     return_list = return_list.next
        
        # return return_list

if __name__ == "__main__":
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    head.print(head)
    head = Solution().sortList(head)
    head.print(head)

