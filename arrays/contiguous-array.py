from typing import List
from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #   Convert all the 0's to -1's
        modified_nums = [0] * len(nums)
        for index, num in enumerate(nums):
            if num == 0:
                modified_nums[index] = -1
            else:
                modified_nums[index] = 1

        #   Calculate the prefix sum for modified_nums
        prefix_sum = [0] * len(modified_nums)
        sum = 0
        for index, num in enumerate(modified_nums):
            sum += num
            prefix_sum[index] = sum

        hash_map = defaultdict(list)
        hash_map[0] = [-1]
        
        max_size = 0
        for index, num in enumerate(prefix_sum):
            if num in hash_map:
                size = index - hash_map[num][0]
                max_size = max(size, max_size)
            hash_map[num].append(index)

        return max_size

if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxLength([0, 1]))
    print(solution.findMaxLength([0, 1, 0]))