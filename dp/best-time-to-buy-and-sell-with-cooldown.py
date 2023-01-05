from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, holding):
            if i >= len(prices):
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            profit = 0
            skip = dp(i + 1, holding)
            if holding:
                profit += max((prices[i] + dp(i + 2, False)), skip)
            elif not holding:
                profit += max((-prices[i] + dp(i + 1, True)), skip)
            memo[(i, holding)] = profit
            return memo[(i, holding)]
        return dp(0, False)

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([1, 2, 3, 0, 2]))
    # print(solution.maxProfit([1, 3, 7, 5, 10, 3]))
    # print(solution.maxProfit([1, 3, 2, 8, 4, 9]))
    # print(solution.maxProfit([1, 3, 7, 5, 10, 3]))