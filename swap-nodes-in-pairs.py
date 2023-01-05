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
    def swapPairs(self, head):
        dummy = head.next
        while head and head.next:
            nextNode = head.next.next
            head.next.next = head

            head.next = nextNode
            head = nextNode


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(Solution().swapPairs(head))