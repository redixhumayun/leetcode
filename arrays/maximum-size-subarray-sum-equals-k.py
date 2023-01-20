from typing import List
from collections import defaultdict

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum = 0
        prefix_sum = [None] * len(nums)
        for index, num in enumerate(nums):
            sum += num
            prefix_sum[index] = sum

        
        hash_map = defaultdict(list)
        hash_map[0] = [-1]
        
        max_size = 0
        for index, num in enumerate(prefix_sum):
            target = num - k
            if target in hash_map:
                size = index - hash_map[target][0]
                max_size = max(max_size, size)
            hash_map[num].append(index)

        return max_size

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArrayLen([1, -1, 5, -2, 3], 3))
    print(solution.maxSubArrayLen([-2, -1, 2, 1], 1))