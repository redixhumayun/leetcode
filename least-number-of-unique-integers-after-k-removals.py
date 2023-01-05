from typing import List
import heapq
from collections import defaultdict

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        occurrences = defaultdict(int)
        for num in arr:
            occurrences[num] += 1
        min_heap = []
        for key, value in occurrences.items():
            heapq.heappush(min_heap, (value, key))
        
        while k > 0:
            occurrences, value = min_heap[0]
            if occurrences == 1:
                heapq.heappop(min_heap)
            else:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (occurrences - 1, value))
            k -= 1
        return len(min_heap)

if __name__ == '__main__':
    s = Solution()
    print(s.findLeastNumOfUniqueInts([5,5,4], 1))
    print(s.findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))