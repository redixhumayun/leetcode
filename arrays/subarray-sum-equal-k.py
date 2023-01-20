from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = defaultdict(int)
        hash_map[0] = 1
        prefix_sum = [-1] * len(nums)
        sum = 0
        for index, num in enumerate(nums):
            sum += num
            prefix_sum[index] = sum

        count = 0
        for index, number in enumerate(prefix_sum):
            look_for = number - k
            if look_for in hash_map:
                count += hash_map[look_for]
            hash_map[number] += 1
        
        return count
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.subarraySum([1, 1, 1], 2))
    print(solution.subarraySum([1,-1,0], 0))