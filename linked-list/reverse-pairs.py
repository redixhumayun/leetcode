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
    def swapPairs(self, head: ListNode):
        if not head:
            return head
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev

if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    ret_val = s.swapPairs(head)
    ret_val.print(ret_val)