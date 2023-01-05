from typing import List
import heapq
from collections import defaultdict

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Build hashmap mapping capital value to indexes where that capital value is available
        # Doing this to prevent having to linearly search array every time for specific capital
        capital_hashmap = defaultdict(list)
        for index, c in enumerate(capital):
            capital_hashmap[c].append(index)
        max_heap = []
        while k:
            temp_w = w
            while not capital_hashmap[temp_w] and temp_w > - 1:
                #   Keep decrementing capital looking for next available capital
                temp_w -= 1
            if temp_w == -1:
                #   Cannot complete k distinct projects
                return w

            available_indexes = capital_hashmap[temp_w]
            for index in available_indexes:
                profit = profits[index]
                heapq.heappush(max_heap, (-profit, index))

            (profit, index) = max_heap[0]
            capital_hashmap[temp_w] = [x for x in capital_hashmap[temp_w] if x != index]    #   Remove the index used from the hashmap
            w += abs(profit)
            k -= 1
        return w
            

if __name__ == '__main__':
    s = Solution()
    print(s.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))
    print(s.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]))
    print(s.findMaximizedCapital(27, 0, [1,2,3], [0,1,2]))
    # print(s.findMaximizedCapital(3, 1, [1,2,3], [1,1,2]))
    # print(s.findMaximizedCapital(3, 0, [1,2,3], [1,2,2]))
    # print(s.findMaximizedCapital(3, 0, [1,2,3], [2,2,2]))
    # print(s.findMaximizedCapital(3, 0, [1,2,3], [2,2,3]))
    # print(s.findMaximizedCapital(3, 0, [1,2,3], [2,3,3]))
    # print(s.findMaximizedCapital(3, 0, [1,2,3], [3,3,3]))
    # print(s.findMaximizedCapital(3, 0, [1,2,3], [3,3,4])) 
    # print(s.findMaximizedCapital(3, 0, [1,2,3], [4,4,5]))
    # print(s.findMaximizedCapital(3, 0, [1,2,3], [4,5,5]))
    # print(s.findMaximizedCapital(3, 0, [1,2,3], [5,5,5]))
    # print(s.findMaximizedCapital(3, 0, [1,2,3], [5,5,6]))
    # print(s.findMaximizedCapital(3, 0, [1,2,3], [5,6,6]))
    # print(s.findMaximizedCapital(3, 0, [1,2,3], [6,6,6]))
    # print(s.findMaximizedCapital(3, 0, [1,2,3], [6,6,7]))
