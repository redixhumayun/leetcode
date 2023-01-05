import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def getMaxHeapLength(self):
        return len(self.max_heap)

    def getMinHeapLength(self):
        return len(self.min_heap)

    def addToMaxHeap(self, num):
        if num < 0:
            #   if num is already negative, don't flip sign
            heapq.heappush(self.max_heap, num)
            return
        heapq.heappush(self.max_heap, -num)
    
    def addToMinHeap(self, num):
        heapq.heappush(self.min_heap, num)

    def popFromMaxHeap(self):
        return abs(heapq.heappop(self.max_heap))

    def popFromMinHeap(self):
        return heapq.heappop(self.min_heap)

    def addNum(self, num: int) -> None:
        if self.getMaxHeapLength() == 0:
            self.addToMaxHeap(num)
            return
        # if self.getMinHeapLength() == 0:
        #     self.addToMinHeap(num)
        #     return
        #   Check if the incoming number is smaller than the max heap's max value
        if num <= abs(self.max_heap[0]):
            #   Check if the difference between the two heap lengths is 1
            heap_diff = self.getMaxHeapLength() - self.getMinHeapLength()
            if heap_diff == 1:
                value = self.popFromMaxHeap()
                self.addToMinHeap(value)
                self.addToMaxHeap(num)
                return
            if heap_diff == 0:
                self.addToMaxHeap(num)
                return
        #   If the incoming number is larger than the max heap's max value
        else:
            heap_diff = self.getMaxHeapLength() - self.getMinHeapLength()
            if heap_diff == 0:
                value = self.popFromMinHeap()
                self.addToMaxHeap(value)
                self.addToMinHeap(num)
                return
            elif heap_diff == 1:
                self.addToMinHeap(num)
                return

    def findMedian(self) -> float:
        heap_diff = self.getMaxHeapLength() - self.getMinHeapLength()
        if heap_diff == 1:
            return abs(self.max_heap[0])
        return (abs(self.max_heap[0]) + self.min_heap[0]) / 2


if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(-1)
    print(obj.findMedian())
    obj.addNum(-2)
    print(obj.findMedian())
    obj.addNum(-3)
    print(obj.findMedian())
    obj.addNum(-4)
    obj.addNum(-5)
    obj.addNum(-6)
    print(obj.findMedian())
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()