class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        memo = {}
        def dp(i, j) -> int:
            if i >= m:
                return n - j

            if j >= n:
                return m - i

            ans = 0
            if (i, j) in memo:
                return memo[(i, j)]

            #   The two characters are equal, do nothing
            if word1[i] == word2[j]:
                ans += dp(i + 1, j + 1)
            #   The two characters are not equal, try all edit operations and minimize
            else:
                #   The edit operations in order are -> insert, replace, delete
                #   Inserting a character into word1 is the same as keeping the pointer at the same place
                #   Replacing a character in word1 with char in word2 is the same as incrementing both pointers
                #   Deleting a char in word1 is the same as incrementing only the i pointer
                ans += 1 + min(dp(i, j+1), dp(i+1, j+1), dp(i+1, j))

            memo[(i, j)] = ans
            return memo[(i, j)]

        return dp(0, 0)
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance("horse", "ros"))
    print(solution.minDistance("intention", "execution"))
    print(solution.minDistance("ab", "bc"))