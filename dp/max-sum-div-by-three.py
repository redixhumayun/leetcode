from typing import List
from functools import cache

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*3 for _ in range(n+1)]
        dp[0][1] = float('-inf')  # type: ignore
        dp[0][2] = float('-inf')  # type: ignore
        for i in range(1, n+1):
            if nums[i-1] % 3 == 0: # Current remainder == 0
                dp[i][0] = max(dp[i-1][0], dp[i-1][0] + nums[i-1]) # Current remainder is 0, so we add to dp[i-1][0] to keep the remainder 0
                dp[i][1] = max(dp[i-1][1], dp[i-1][1] + nums[i-1]) # Current remainder is 0, so we add to dp[i-1][1] to keep the remainder 1
                dp[i][2] = max(dp[i-1][2], dp[i-1][2] + nums[i-1]) # Current remainder is 0, so we add to dp[i-1][2] to keep the remainder 2
            elif nums[i-1] % 3 == 1: # Current remainder == 1
                dp[i][0] = max(dp[i-1][0], dp[i-1][2] + nums[i-1]) # Current remainder is 1, so we add to dp[i-1][2] to keep the remainder 0
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] + nums[i-1]) # Current remainder is 1, so we add to dp[i-1][0] to keep the remainder 1
                dp[i][2] = max(dp[i-1][2], dp[i-1][1] + nums[i-1]) # Current remainder is 1, so we add to dp[i-1][1] to keep the remainder 2
            else: # Current remainder == 2
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + nums[i-1]) # Can you tell how this works now?
                dp[i][1] = max(dp[i-1][1], dp[i-1][2] + nums[i-1])
                dp[i][2] = max(dp[i-1][2], dp[i-1][0] + nums[i-1])

        return dp[-1][0]
    # def maxSumDivThree(self, nums: List[int]):
    #     memo = {}
    #     def dp(index, remainder):
    #         if index == len(nums):
    #             if remainder % 3 == 0:
    #                 return remainder
    #             return float("-inf")
            
    #         if (index, remainder) in memo:
    #             return memo[(index, remainder)]
    #         ans = 0
    #         remainder_with_skip = dp(index + 1, remainder % 3)
    #         remainder_without_skip = nums[index] + dp(index + 1, (remainder + nums[index]) % 3)
    #         ans = max(remainder_without_skip, remainder_with_skip)
    #         memo[(index, remainder)] = ans
    #         return memo[(index, remainder)]
    #     return dp(0, 0)
        # def dp(index, sum):
        #     if index == len(nums):
        #         return sum
        #     if (index, sum) in memo:
        #         return memo[(index, sum)]
            
        #     ans = 0
        #     sum_with_skip = dp(index + 1, sum)
        #     sum_without_skip = dp(index + 1, sum + nums[index])

        #     if sum_with_skip % 3 == 0:
        #         ans = max(ans, sum_with_skip)
        #     if (sum_without_skip) % 3 == 0:
        #         ans = max(ans, sum_without_skip)
        #     memo[(index, sum)] = ans
        #     return memo[(index, sum)]
        # return dp(0, 0)

if __name__ == '__main__':
    print(Solution().maxSumDivThree([3,6,5,1,8]))
    print(Solution().maxSumDivThree([4]))
    print(Solution().maxSumDivThree([1,2,3,4,4]))
    print(Solution().maxSumDivThree([2,6,2,2,7]))
    print(Solution().maxSumDivThree([783,843,806,408,560,215,113,186,461,443,498,364,127,645,554,383,88,522,366,888,372,194,914,546,341,568,957,773,48,623,783,322,675,514,920,826,670,964,204,156,45,759,599,390,627,39,194,560,326,523,370,286,917,943,346,927,181,287,114,217,292,240,441,893,603,595,908,719,138,86,767,52,904,771,846,871,177,228,848,619,951,446,425,914,611,205,568,845,439,399,133,286,408,93,410,287,680,332,14,882]))
    # print(Solution().maxSumDivThree([1,2,3,4,4]))
    # print(Solution().maxSumDivThree([2,6,2,2,7]))
    # print(Solution().maxSumDivThree([1,2,3,4,4]))
    # print(Solution().maxSumDivThree([2,6,2,2,7]))
    # print(Solution().maxSumDivThree([1,2,3,4,4]))
    # print(Solution().maxSumDivThree([2,6,2,2,7]))
    # print(Solution().maxSumDivThree([1,2,3,4,4]))
    # print(Solution().maxSumDivThree([2,6,2,2,7]))
    # print(Solution().maxSumDivThree([1,2,3,4,4]))
    # print(Solution().maxSumDivThree([2,6,2,2,7]))
    # print(Solution().maxSumDivThree([1,2,3,4,4]))
    # print(Solution().maxSumDivThree([2,6,2,2,7]))
    # print(Solution().maxSumDivThree([1,2,3,4,4]))
    # print(Solution().maxSumDivThree([2,6,2,2,7]))
    # print(Solution().maxSumDivThree([1,2,3,4,4]))
    # print(Solution().maxSumDivThree([2,6,2,2,7]))
    # print(Solution().maxSumDivThree([1,2,3,4,4]))
    # print(Solution().maxSumDivThree([2,6,2,2,7]))
    # print(Solution().maxSumDivThree([1,2,3,4,4]))
    # print(Solution().maxSumDivThree([2,6,2,2,7]))
    # print(Solution().maxSumDivThree([1,2,3,4,4]))