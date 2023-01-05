from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        #iterative
        def dp_iterative(n):
            dp = [0] * (n + 1)
            dp[0] = 1
            dp[1] = 1
            for i in range(2, n+1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n]

        def dp(n):
            if n <= 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = dp(n-1) + dp(n-2)
            return memo[n]
        return dp_iterative(n)


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(1))
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
    # print(solution.climbStairs(4))
    # print(solution.climbStairs(5))
    # print(solution.climbStairs(6))
    # print(solution.climbStairs(7))
    # print(solution.climbStairs(8))
    # print(solution.climbStairs(9))
    # print(solution.climbStairs(10))
    # print(solution.climbStairs(11))
    # print(solution.climbStairs(12))
    # print(solution.climbStairs(13))
    # print(solution.climbStairs(14))
    # print(solution.climbStairs(15))
    # print(solution.climbStairs(16))
    # print(solution.climbStairs(17))
    # print(solution.climbStairs(18))
    # print(solution.climbStairs(19))
    # print(solution.climbStairs(20))
    # print(solution.climbStairs(21))
    # print(solution.climbStairs(22))
    # print(solution.climbStairs(23))
    # print(solution.climbStairs(24))
    # print(solution.climbStairs(25))
    # print(solution.climbStairs(26))
    # print(solution.climbStairs(27))
    # print(solution.climbStairs(28))
    # print(solution.climbStairs(29))
    # print(solution.climbStairs(30))
    # print(solution.climbStairs(31))
    # print(solution.climbStairs(32))
    # print(solution.climbStairs(33))
    # print(solution.climbStairs(34))
    # print(solution.climbStairs(35))
    # print(solution.climbStairs(36))
    # print(solution.climbStairs(37))
    # print(solution.climbStairs(38))
    # print(solution.climbStairs(39))
    # print(solution.climbStairs(40))
    # print(solution.climbStairs(41))
    # print(solution.climbStairs(42))
    # print(solution.climbStairs(43))
    # print(solution.climbStairs(44))
    # print(solution.climbStairs(45))