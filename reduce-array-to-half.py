from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hashmap = defaultdict(int)
        for num in arr:
            hashmap[num] += 1
        max_heap = []
        for key, value in hashmap.items():
            heapq.heappush(max_heap, (-value, key))
        
        orig_length = len(arr)
        count = 0
        while orig_length > len(arr) // 2:
            occurrences, number = heapq.heappop(max_heap)
            count += 1
            orig_length -= abs(occurrences)
        return count

print(Solution().minSetSize([3,3,3,3,5,5,5,2,2,7]))
print("***")
print(Solution().minSetSize([7,7,7,7,7,7]))
print("***")
print(Solution().minSetSize([1, 9]))