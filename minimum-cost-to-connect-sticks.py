import heapq

class Solution:
    def connectSticks(self, sticks) -> int:
        if len(sticks) == 1:
            return 0
        min_heap = []
        for stick in sticks:
            heapq.heappush(min_heap, stick)
        
        sum_of_work = 0
        while len(min_heap) > 1:
            value_1 = heapq.heappop(min_heap)
            value_2 = heapq.heappop(min_heap)
            result = value_1 + value_2
            sum_of_work += result
            heapq.heappush(min_heap, result)
        return sum_of_work

if __name__ == '__main__':
    sticks = [5]
    print(Solution().connectSticks(sticks))