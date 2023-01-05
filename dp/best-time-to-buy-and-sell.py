from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = {}
        def dp(i, k, holding) -> int:
            if i == len(prices):
                return 0
            if k == 0:
                return 0
            if (i, k, holding) in memo:
                return memo[(i, k, holding)]
            profit = 0
            if not holding:
                buying = -prices[i] + dp(i + 1, k, True)
                not_buying = dp(i + 1, k, holding)
                profit += max(buying, not_buying)
            else:
                selling = prices[i] + dp(i + 1, k - 1, False)
                not_selling = dp(i + 1, k, holding)
                profit += max(selling, not_selling)
            memo[(i, k, holding)] = profit
            return memo[(i, k, holding)]
        return dp(0, k, False)

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit(2, [2, 4, 1]))
    print(solution.maxProfit(2, [3, 2, 6, 5, 0, 3]))