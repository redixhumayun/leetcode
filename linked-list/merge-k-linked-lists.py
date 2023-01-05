
"""
For your reference:
"""
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print(self, head):
        while head:
            print(head.value, end=" ")
            head = head.next
        print("\n")

def merge_k_lists(lists):
    """
    Args:
     lists(list_LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.

    #   Alternate approach
    

    array = []
    for list in lists:
        head = list
        while head is not None:
            array.append(head.value)
            head = head.next
    
    array.sort()
    new_list_head = LinkedListNode(0)
    temp = new_list_head
    for num in array:
        temp.next = LinkedListNode(0)  # type: ignore
        temp = temp.next
        temp.value = num
    
    new_list_head = new_list_head.next
    return new_list_head

if __name__ == '__main__':
    list1 = LinkedListNode(1)
    list1.next = LinkedListNode(3)
    list1.next.next = LinkedListNode(5)
    list2 = LinkedListNode(2)
    list2.next = LinkedListNode(4)
    list2.next.next = LinkedListNode(6)
    list3 = LinkedListNode(7)
    lists = [list1, list2, list3]
    merge_k_lists(lists)

    