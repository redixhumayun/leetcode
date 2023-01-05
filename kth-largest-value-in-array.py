import heapq

class KthLargest:

    def __init__(self, k: int, nums):
        self.min_heap = []
        self.max_heap = []
        self.min_heap_max_size = k - 1
        self.nums = nums
        self.initHeap()

    def initHeap(self):
        for num in self.nums:
            self.add(num)
        return None

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.min_heap_max_size:
            heapq.heappush(self.min_heap, val)
            return None
        heapq.heappush(self.min_heap, val)
        value = heapq.heappop(self.min_heap)
        heapq.heappush(self.max_heap, -value)
        return abs(self.max_heap[0])
            
if __name__ == '__main__':
    k = 3
    nums = [1, 2, 3, 4]
    kthLargest = KthLargest(k, nums)
    print(kthLargest.add(5))
    print(kthLargest.add(6))
    print(kthLargest.add(7))
    print(kthLargest.add(8))
    print(kthLargest.add(9))

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)