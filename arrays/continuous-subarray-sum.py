from collections import defaultdict
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1 and nums[0] == 0 and k != 0:
            return False
        hash_map = defaultdict(int)
        hash_map[0] = 0
        prefix_sum = [None] * len(nums)
        sum = 0
        for index, num in enumerate(nums):
            sum += num
            prefix_sum[index] = sum

        prefix_sum_mod = [num % k for num in prefix_sum]

        for num in prefix_sum_mod:
            if num in hash_map:
                return True
            hash_map[num] = 0
        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.checkSubarraySum([23, 2, 4, 6, 7], 6))
    # print(solution.checkSubarraySum([23, 2, 6, 4, 7], 6))
    print(solution.checkSubarraySum([23, 2, 6, 4, 7], 13))
    print(solution.checkSubarraySum([23, 2, 4, 6, 6], 7))
    # print(solution.checkSubarraySum([0, 0], 0))
    # print(solution.checkSubarraySum([0, 1, 0], 0))
    # print(solution.checkSubarraySum([0, 1, 0], 1))