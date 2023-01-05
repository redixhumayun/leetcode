from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(amt):
            ans = float("inf")
            if amt < 0:
                return -1
            if amt == 0:
                return 0
            if amt in memo:
                return memo[amt]
            for coin in coins:
                result = dp(amt - coin)
                print(amt, result)
                if result != -1:
                    memo[amt] = min(ans, result + 1)
            if ans != float("inf"):
                return memo[amt]
            return -1
            # if amt not in memo:
            #     return -1
            # return memo[amt]
        return dp(amount)

# from functools import lru_cache
# from typing import List

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> float | int:

#         @lru_cache(None)
#         def dfs(rem):
#             if rem < 0:
#                 return -1
#             if rem == 0:
#                 return 0
#             min_cost = float('inf')
#             for coin in coins:
#                 res = dfs(rem - coin)
#                 if res != -1:
#                     min_cost = min(min_cost, res + 1)
#             return min_cost if min_cost != float('inf') else -1

#         return dfs(amount)
            

if __name__ == '__main__':
    solution = Solution()
    # print(solution.coinChange([1, 2, 5], 11))
    # print(solution.coinChange([2], 3))
    # print(solution.coinChange([1], 0))
    # print(solution.coinChange([1], 1))
    # print(solution.coinChange([1], 2))
    # print(solution.coinChange([2], 1))
    print(solution.coinChange([186,419,83,408], 6249))