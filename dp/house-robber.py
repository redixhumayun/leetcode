from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i):
            if i < 0:
                return 0
            if i == 0 or i == 1:
                return nums[i]
            if i in memo:
                return memo[i]
            
            cost_of_robbing_two_houses_away = dp(i-2)
            cost_of_robbing_three_houses_away = dp(i-3)
            memo[i] = nums[i] + max(cost_of_robbing_two_houses_away, cost_of_robbing_three_houses_away)
            return memo[i]        
        memo = {}
        return max(dp(len(nums) - 1), dp(len(nums) - 2))

if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([1, 2, 3, 1]))
    print(solution.rob([1, 7, 5, 4, 2, 8, 6, 1, 11]))
    print(solution.rob([2, 7, 9, 3, 1]))
    print(solution.rob([2, 1, 1, 2]))