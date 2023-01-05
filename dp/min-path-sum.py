from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int | float:
        #   DP approach with memoization
        m = len(grid)
        n = len(grid[0])
        def dp(row, col) -> int | float:
            if row + col == 0:
                #   Base case - reached the 0th cell
                return grid[row][col]
            path_sum = float("inf")
            if row > 0:
                path_sum = min(path_sum, grid[row][col] + dp(row - 1, col))
            if col > 0:
                path_sum = min(path_sum, grid[row][col] + dp(row, col - 1))
            return path_sum
        return dp(m - 1, n - 1)

        #   This is the classic backtracking DFS approach with memoization
        # m = len(grid)
        # n = len(grid[0])
        # valid_directions = [(1, 0), (0, 1)]
        # memo = {}

        # def is_valid(row, col):
        #     return 0 <= row < m and 0 <= col < n

        # def dp(row, col):
        #     if row == m - 1 and col == n - 1:
        #         return grid[row][col]
        #     if (row, col) in memo:
        #         return memo[(row, col)]
        #     path_sum = float("inf")
        #     for dx, dy in valid_directions:
        #         new_row, new_col = row + dx, col + dy
        #         if is_valid(new_row, new_col):
        #             path_sum = min(path_sum, grid[row][col] + dp(new_row, new_col))
        #     memo[(row, col)] = path_sum
        #     return memo[(row, col)]
        # return dp(0, 0)

if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(s.minPathSum([[1,2,3],[4,5,6]]))