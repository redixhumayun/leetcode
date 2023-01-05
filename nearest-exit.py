from collections import deque

class Solution:
    def nearestExit(self, maze, entrance) -> int:
        row_size = len(maze)
        col_size = len(maze[0])

        def isValidCell(row, col):
            return 0 <= row < row_size and 0 <= col < col_size

        def isValidExit(row, col):
            return isValidCell(row, col) \
            and ((row == 0 or row == row_size - 1) or (col == 0 or col == col_size - 1)) \
            and maze[row][col] == "." \
            and (row, col) != (entrance[0], entrance[1])

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        queue = deque()
        queue.append((entrance[0], entrance[1], 0)) #   row, col, steps
        seen = {(entrance[0], entrance[1])}
        ans = float("inf")

        while queue:
            (row, col, steps) = queue.popleft()
            if isValidExit(row, col):
                ans = min(ans, steps)
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if isValidCell(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    if maze[new_row][new_col] != "+":
                        #   This path is not blocked
                        queue.append((new_row, new_col, steps + 1))
        
        if ans == float("inf"):
            #   no path found
            return -1
        return ans

if __name__ == '__main__':
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1,2]
    print(Solution().nearestExit(maze, entrance))