class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #   Iterative solution - bottom up approach
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n+1)]for _ in range(m)]

        if text1[m-1] == text2[n-1]:
            dp[m-1][n-1] = 1

        for i in range(n-2, -1, -1):
            dp[m-1][i] = dp[m-1][i+1]
            if text1[m-1] == text2[i]:
                dp[m-1][i] += 1


        for i in range(m - 2, -1, -1):
            ans = 0
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    ans = dp[i+1][j+1] + 1
                else:
                    ans = max(dp[i+1][j], dp[i][j+1])
                dp[i][j] = ans

        return dp[0][0]


        # m = len(text1)
        # n = len(text2)
        # memo = {}
        # def dp(i, j) -> int:
        #     if i == m or j == n:
        #         return 0
        #     ans = 0
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     if text1[i] == text2[j]:
        #         ans += 1 + dp(i + 1, j + 1)
        #     elif text1[i] != text2[j]:
        #         ans += max(dp(i+1, j), dp(i, j+1))
        #     memo[(i, j)] = ans
        #     return memo[(i, j)]
        
        # return dp(0, 0)

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonSubsequence("abcde", "ace"))
    print(solution.longestCommonSubsequence("abc", "abc"))
    print(solution.longestCommonSubsequence("abc", "def"))
    print(solution.longestCommonSubsequence("ylqpejqbalahwr", "yrkzavgdmdgtqpg"))