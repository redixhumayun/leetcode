from collections import defaultdict

class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, value=None):
        self.head = LinkedListNode(value)
        self.head_reference = self.head

    def insert(self, value):
        if self.head.value is None:
            self.head.value = value
            self.head_reference = self.head
            return
        self.head.next = LinkedListNode(value)
        self.head = self.head.next


class LRUCache:

    def __init__(self, capacity: int):
        self.key_value_hash_map = defaultdict(int)
        self.capacity = capacity
        self.linked_list = LinkedList()
        self.linked_list_count = defaultdict(int)
        

    def get(self, key: int) -> int:
        if key in self.key_value_hash_map:
            self.linked_list.insert(key)
            self.linked_list_count[key] += 1
            return self.key_value_hash_map[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        #   Check if this value already exists
        if key in self.key_value_hash_map:
            self.key_value_hash_map[key] = value
            
            #   Update the linked list
            self.linked_list.insert(key)
            self.linked_list_count[key] += 1

        else:
            #   Check if there is enough capacity
            if len(self.key_value_hash_map) + 1 <= self.capacity:
                self.key_value_hash_map[key] = value
                self.linked_list.insert(key)
                self.linked_list_count[key] += 1

            #   If there is not enough capacity
            else:
                self.remove_least_recently_used_key()
                self.key_value_hash_map[key] = value
                self.linked_list.insert(key)
                self.linked_list_count[key] += 1
                pass

    def remove_least_recently_used_key(self):
        prev = None
        head = self.linked_list.head_reference
        while head is not None:
            node_count_value = self.linked_list_count[head.value]
            temp = head.value
            if node_count_value == 1:
                #   This is the only occurrence of the node

                #   If this is not the head node
                if prev is not None:
                    prev.next = head.next
                #   if this is the head node
                else:
                    head = head.next
                    self.linked_list.head = head
                    self.linked_list.head_reference = head
                
                #   remove the key from the hash map as well and linked_list_count
                del self.linked_list_count[temp]
                del self.key_value_hash_map[temp]
                return
            else:
                #   This is not the only occurrence of the node

                #   If this is not the head node
                if prev is not None:
                    prev.next = head.next
                    head = head.next
                else:
                    head = head.next
                    self.linked_list.head = head
                    self.linked_list.head_reference = head
                self.linked_list_count[temp] -= 1
        
if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))       # returns 1
    cache.put(3, 3)    # evicts key 2
    print(cache.get(2))       # returns -1 (not found)
    cache.put(4, 4)    # evicts key 1
    print(cache.get(1))       # returns -1 (not found)
    print(cache.get(3))       # returns 3
    print(cache.get(4))       # returns 4

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)