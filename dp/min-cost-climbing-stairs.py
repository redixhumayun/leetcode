from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #   Iterative
        def dp_iterative(n):
            dp = [0] * n
            dp[0] = cost[0]
            dp[1] = cost[1]
            for i in range(2, n):
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            return min(dp[n-1], dp[n-2])

        memo = {}
        def dp(n):
            if n < 0:
                return 0
            if n == 0 or n == 1:
                return cost[n]
            if n in memo:
                return memo[n]
            cost_of_reaching_1_step_away = dp(n-1)
            cost_of_reaching_2_step_away = dp(n-2)
            memo[n] = cost[n] + min(cost_of_reaching_1_step_away, cost_of_reaching_2_step_away)
            return memo[n]
        return dp_iterative(len(cost))
        # return min(dp(len(cost) - 1), dp(len(cost) - 2))

if __name__ == '__main__':
    solution = Solution()
    print(solution.minCostClimbingStairs([10, 15, 20]))
    print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print(solution.minCostClimbingStairs([0, 0, 0, 0]))
    print(solution.minCostClimbingStairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(solution.minCostClimbingStairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))