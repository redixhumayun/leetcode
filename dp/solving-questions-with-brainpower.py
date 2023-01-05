from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        #   Bottom up implementation
        def dp_iterative():
            n = len(questions)
            dp = [0] * (len(questions) + 1)
            for i in range(len(questions) - 1, -1, -1):
                j = i + questions[i][1] + 1
                dp[i] = max(questions[i][0] + dp[min(n, j)], dp[i+1])
            return dp[0]
        def dp(i):
            if i >= len(questions):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(questions[i][0] + dp(i + questions[i][1] + 1), dp(i+1))
            return memo[i]
        return dp(0)

if __name__ == '__main__':
    solution = Solution()
    print(solution.mostPoints([[3,2],[4,3],[4,4],[2,5]]))
    print(solution.mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]))