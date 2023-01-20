from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def is_valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        set_of_2 = set()
        queue_of_2 = deque()
        
        #   preprocess grid to find all 2's
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    set_of_2.add((i, j))
                    queue_of_2.append((i, j))

        #   iterate through list of 2's and keep adding to it
        count = 0
        change_flag = False
        while len(queue_of_2) > 0:
            change_flag = False
            current_length = len(queue_of_2)
            for _ in range(current_length):
                (row, col) = queue_of_2.popleft()
                for (dx, dy) in directions:
                    new_row, new_col = row + dx, col + dy
                    if is_valid(new_row, new_col) and grid[new_row][new_col] == 1:
                        change_flag = True
                        grid[new_row][new_col] = 2
                        queue_of_2.append((new_row, new_col))
            if change_flag is True:
                count += 1
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1

        return count

if __name__ == "__main__":
    print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
    print(Solution().orangesRotting([[0,2]]))
    print(Solution().orangesRotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]]))