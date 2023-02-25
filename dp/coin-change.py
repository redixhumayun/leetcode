from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #   Iterative solution
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, len(dp)):
            ans = float("inf")
            for coin in coins:
                if coin <= i:
                    ans = min(ans, dp[i - coin] + 1)
            dp[i] = ans
        if dp[-1] == float("inf"):
            return -1
        return dp[-1]

        # memo = {}
        # def dp(amount):
        #     if amount == 0:
        #         return 0

        #     if amount in memo:
        #         return memo[amount]

        #     ans = float("inf")
        #     for coin in coins:
        #         if coin <= amount:
        #             ans = dp(amount - coin) + 1
        #         memo[amount] = min(memo.get(amount, float("inf")), ans)
        #     return memo[amount]
        # result = dp(amount)

        # if result == float("inf"):
        #     return -1
        # return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 100))
    print(solution.coinChange([2], 3))
    print(solution.coinChange([2,5,10,1], 27))