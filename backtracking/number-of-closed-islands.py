from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        def is_on_border(row, col):
            return row == 0 or row == m - 1 or col == 0 or col == n - 1

        def backtrack(row, col):
            result = True
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if valid(new_row, new_col) and (new_row, new_col) not in seen and grid[new_row][new_col] == 0:
                    seen.add((new_row, new_col))
                    if is_on_border(new_row, new_col):
                        #   If I have reached the border and encountered a zero, this is not an island
                        result = False
                    result = backtrack(new_row, new_col) and result
            return result
            

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()
        number_of_islands = 0
        for row in range(1, m - 1):
            for col in range(1, n - 1):
                if grid[row][col] == 0 and (row, col) not in seen:
                    seen.add((row, col))
                    result = backtrack(row, col)
                    if result == True:
                        number_of_islands += 1
        return number_of_islands


if __name__ == '__main__':
    # print(Solution().closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))
    # print(Solution().closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))
    # print(Solution().closedIsland([[1,1,1,1,1,1,1],
    #                                 [1,0,0,0,0,0,1],
    #                                 [1,0,1,1,1,0,1],
    #                                 [1,0,1,0,1,0,1],
    #                                 [1,0,1,1,1,0,1],
    #                                 [1,0,0,0,0,0,1],
    #                                 [1,1,1,1,1,1,1]]))
    print(Solution().closedIsland([[1,0,1,1,1,1,0,0,1,0],
                                    [1,0,1,1,0,0,0,1,1,1],
                                    [0,1,1,0,0,0,1,0,0,0],
                                    [1,0,1,1,0,1,0,0,1,0],
                                    [0,1,1,1,0,1,0,1,0,0],
                                    [1,0,0,1,0,0,1,0,0,0],
                                    [1,0,1,1,1,0,0,1,1,0],
                                    [1,1,0,1,1,0,1,0,1,1],
                                    [0,0,1,1,1,0,1,0,1,1],
                                    [1,0,0,1,1,1,1,0,1,1]]))