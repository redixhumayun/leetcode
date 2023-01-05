class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #   Iterative approach
        dp = []
        for _ in range(m):
            dp.append([0] * n)
        dp[0][0] = 1
        def dfs_iterative():
            for row in range(m):
                for col in range(n):
                    if row > 0:
                        dp[row][col] += dp[row - 1][col]
                    if col > 0:
                        dp[row][col] += dp[row][col - 1]
            return dp
        dfs_iterative()
        return dp[m-1][n-1]

        # def is_valid(row, col):
        #     return 0 <= row < m and 0 <= col < n
        # valid_directions = [(1, 0), (0, 1)]
        # memo = {}
        # def dfs(row, col) -> int:
        #     if row == m - 1 and col == n - 1:
        #         #   Reached last cell
        #         return 1
        #     if (row, col) in memo:
        #         return memo[(row, col)]
        #     ans = 0
        #     for dx, dy in valid_directions:
        #         new_row, new_col = row + dx, col + dy
        #         if is_valid(new_row, new_col):
        #             ans += dfs(new_row, new_col)
        #     memo[(row, col)] = ans
        #     return memo[(row, col)]
        # return dfs(0, 0)

if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(3, 2))
    # print(solution.uniquePaths(3, 7))
    # print(solution.uniquePaths(7, 3))
    # print(solution.uniquePaths(1, 1))