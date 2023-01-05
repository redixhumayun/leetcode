from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int | float:
        m = len(matrix)
        n = len(matrix[0])

        #   Bottom up DP solution with O(N) space
        row = [0] * (n+1)

        for r in range(m-1, -1, -1):
            new_row = [0] * (n+1)
            for c in range(n):
                if c == 0:
                    new_row[c] = matrix[r][c] + min(row[c], row[c+1])
                elif c == n - 1:
                    new_row[c] = matrix[r][c] + min(row[c], row[c-1])
                else:
                    new_row[c] = matrix[r][c] + min(row[c], min(row[c+1], row[c-1]))
            row = new_row
        row.pop()
        return min(row)

        #   Bottom up DP solution
        # dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        # for row in range(m-1, -1, -1):
        #     for col in range(n-1, -1, -1):
        #         if col == 0:
        #             dp[row][col] = matrix[row][col] + min(dp[row+1][col+1], dp[row+1][col])
        #         elif col == n-1:
        #             dp[row][col] = matrix[row][col] + min(dp[row+1][col], dp[row+1][col-1])
        #         else:
        #             dp[row][col] = matrix[row][col] + min(dp[row+1][col+1], min(dp[row+1][col], dp[row+1][col-1]))
        # ans = float("inf")
        # for i in range(len(dp[0]) - 1):
        #     ans = min(ans, dp[0][i])
        # return ans

        # memo = {}

        # def is_valid(row, col):
        #     return 0 <= row < m and 0 <= col < n

        # directions = [(-1, -1), (-1, 0), (-1, 1)]

        # def dp_alternate(row, col):
        #     if row == 0:
        #         #   Base case, first row
        #         return matrix[row][col]
        #     if (row, col) in memo:
        #         return memo[(row, col)]
        #     ans = float("inf")
        #     for dx, dy in directions:
        #         new_row, new_col = row + dx, col + dy
        #         if is_valid(new_row, new_col):
        #             ans = min(ans, matrix[row][col] + dp_alternate(new_row, new_col))
        #         memo[(row, col)] = ans
        #     return memo[(row, col)]
            
        # ans = float("inf")
        # for col in range(n):
        #     ans = min(ans, dp_alternate(m - 1, col))
        # return ans

        # directions = [(1, -1), (1, 0), (1, 1)]

        # def dp(row, col):
        #     if row == m - 1:
        #         #   Base case, last row
        #         return matrix[row][col]
        #     if (row, col) in memo:
        #         return memo[(row, col)]
        #     ans = float("inf")
        #     for dx, dy in directions:
        #         new_row, new_col = row + dx, col + dy
        #         if is_valid(new_row, new_col):
        #             ans = min(ans, matrix[row][col] + dp(new_row, new_col))
        #     memo[(row, col)] = ans
        #     return memo[(row, col)]
        
        # ans = float("inf")
        # for col in range(n):
        #     #   Iterate over the entire first row
        #     ans = min(ans, dp(0, col))
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
    print(s.minFallingPathSum([[-19,57],[-40,-5]]))
