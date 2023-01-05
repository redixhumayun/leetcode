from typing import List
from functools import cache

# class Solution:
#     def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
#         @cache
#         def dp(i, remain):
#             if i == len(piles) or remain == 0:
#                 return 0
            
#             ans = dp(i + 1, remain) # skip this pile
#             curr = 0
#             for j in range(min(remain, len(piles[i]))):
#                 curr += piles[i][j]
#                 ans = max(ans, curr + dp(i + 1, remain - j - 1))
            
#             return ans

#         return dp(0, k)

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int | float:
        def dp(piles_count: list, current_pile_index, k) -> int | float:
            if piles_count[current_pile_index] >= len(piles[current_pile_index]):
                return 0
            if k == 0:
                return 0
            ans = 0
            for index, variable in enumerate(piles_count):
                incremented_piles = piles_count[:]
                incremented_piles[index] += 1
                ans = max(ans, piles[index][variable] + dp(incremented_piles, index, k - 1))
            return ans
        piles_count = [0] * len(piles)
        return dp(piles_count, 0, k)

if __name__ == '__main__':
    solution = Solution()
    piles = [[1,100,3],[7,8,9]]
    k = 2
    print(solution.maxValueOfCoins(piles, k))

    piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]]
    k = 7
    print(solution.maxValueOfCoins(piles, k))

    piles = [[37,88],[51,64,65,20,95,30,26],[9,62,20],[44]]
    k = 9
    print(solution.maxValueOfCoins(piles, k))