class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = {}
        def dp(i, j) -> int:
            if i == m or j == n:
                return 0
            ans = 0
            if (i, j) in memo:
                return memo[(i, j)]
            if text1[i] == text2[j]:
                ans += 1 + dp(i + 1, j + 1)
            elif text1[i] != text2[j]:
                ans += max(dp(i+1, j), dp(i, j+1))
            memo[(i, j)] = ans
            return memo[(i, j)]
        
        return dp(0, 0)

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonSubsequence("abcde", "ace"))
    print(solution.longestCommonSubsequence("abc", "abc"))
    print(solution.longestCommonSubsequence("abc", "def"))
    print(solution.longestCommonSubsequence("ylqpejqbalahwr", "yrkzavgdmdgtqpg"))