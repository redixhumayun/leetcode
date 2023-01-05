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
    def pairSum(self, head) -> int:
        #   Find the middle of the linked list
        fastPointer = head
        slowPointer = head
        list_size_counter = 0
        while fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            list_size_counter += 2
            slowPointer = slowPointer.next
        
        #   Get the end of the first half of the list
        first_tail = head
        middle = list_size_counter // 2
        for i in range(middle - 1):
            first_tail = first_tail.next
        
        #   Slow pointer is the middle value and first_tail is the end of the first linked list
        #   Reverse the remainder of the linked list starting at slowPointer
        prev = None
        curr = slowPointer
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        first_tail.next = prev
        
        #   use fast and slow pointer again to find head and middle of the list
        slowPointer = fastPointer = head
        for i in range(middle):
            fastPointer = fastPointer.next
        ans = 0
        while fastPointer:
            ans = max(ans, slowPointer.val + fastPointer.val)
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
        return ans

if __name__ == '__main__':
    head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
    # print(Solution().pairSum(head))
    Solution().pairSum(head)