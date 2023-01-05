from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #   This is the O(n) approach
        seen = defaultdict(int)
        for index, num in enumerate(nums):
            x = target - num
            if x in seen:
                return [seen[x], index]
            seen[num] = index

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    C = Solution()
    print(C.twoSum(nums, target))

    nums = [3, 2, 4]
    target = 6
    C = Solution()
    print(C.twoSum(nums, target))

    nums = [3, 3]
    target = 6
    C = Solution()
    print(C.twoSum(nums, target))