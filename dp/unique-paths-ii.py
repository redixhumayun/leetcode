from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        valid_directions = [(0, 1), (1, 0)]
        memo = {}
        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n and obstacleGrid[row][col] == 0
        def dfs(row, col):
            if obstacleGrid[row][col] == 1:
                #   Edge case of the starting point being 0
                return 0
            if row == m - 1 and col == n - 1:
                #   Base case
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
            ans = 0
            for dx, dy in valid_directions:
                new_row, new_col = row + dx, col + dy
                if is_valid(new_row, new_col):
                    ans += dfs(new_row, new_col)
            memo[(row, col)] = ans
            return memo[(row, col)]
        return dfs(0, 0)
            


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    print(s.uniquePathsWithObstacles([[0,1],[0,0]]))
    print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0],[0,0,0]]))