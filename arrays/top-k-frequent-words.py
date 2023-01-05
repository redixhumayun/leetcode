from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #   Create a hashmap of the words
        counter = defaultdict(int)
        for word in words:
            counter[word] += 1
        #   Create a min heap from all the words
        min_heap = []
        for key, value in counter.items():
            heapq.heappush(min_heap, (value, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            print(min_heap)
        result = [None] * k
        print(min_heap)
        previous_value = None
        previous_key = None
        index = 0
        for value, key in reversed(min_heap):
            if value == previous_value:
                #   Same frequency, sort by lexicographical order instead
                temp = result[index-1]
                result[index-1] = key
                result[index] = temp
                index += 1
                continue
            previous_value = value
            previous_key = key
            result[index] = key
            index += 1
        return result

if __name__ == '__main__':
    words = ["i","love","leetcode","i","love","coding"]
    k = 1
    print(Solution().topKFrequent(words, k))