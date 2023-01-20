from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = min_so_far = 1
        result = max(nums)
        for index, number in enumerate(nums):
            temp = max_so_far
            max_so_far = max(max_so_far * number, min_so_far * number, number)
            min_so_far = min(min_so_far * number, temp * number, number)
            result = max(result, max_so_far)
        return result

if __name__ == "__main__":
    print(Solution().maxProduct([2, 3, -2, 4]))
    print(Solution().maxProduct([-1, -2, -3]))
    print(Solution().maxProduct([2,-5,-2,-4,3]))
    print(Solution().maxProduct([2,0,-1]))