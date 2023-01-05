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
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        prev.print(prev)

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(Solution().reverseList(head))


#########
# 1->2->3->4
# should result in
# 4->3->2->1
#
#
#########