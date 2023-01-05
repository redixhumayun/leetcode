import heapq
import math

class Solution:
    def minStoneSum(self, piles, k: int) -> int:
        max_heap = []
        s = 0
        for p in piles:
            s += p
            heapq.heappush(max_heap, -p)
        
        while k > 0:
            largest_value = abs(heapq.heappop(max_heap))
            operation = math.floor(largest_value / 2)
            result = largest_value - operation
            s -= operation
            heapq.heappush(max_heap, -result)
            k -= 1
        return s
        
if __name__ == '__main__':
    piles = [4,3,6,7]
    k = 3
    print(Solution().minStoneSum(piles, k))