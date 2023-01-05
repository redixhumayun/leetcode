from functools import cache
from typing import List

class Solution:
    #   Bottom up implementation
    def lengthOfLISIterative(self, nums):
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            ans = 1 # Base case

            # Recurrence relation
            for j in range(i):
                if nums[i] > nums[j]:
                    ans = max(ans, dp(j) + 1)
            
            return ans

        return max(dp(i) for i in range(len(nums)))

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLISIterative([10, 9, 2, 5, 3, 7, 101, 18]))
    print(solution.lengthOfLISIterative([0, 1, 0, 3, 2, 3]))
# if __name__ == "__main__":
#     solution = Solution()
    # print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    # print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))
    # print(solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
    # print(solution.lengthOfLIS([4, 10, 4, 3, 8, 9]))