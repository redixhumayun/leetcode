from collections import deque
def max_island_size(grid):
    """
    Args:
     grid(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    m = len(grid)
    n = len(grid[0])

    def is_valid(row, col):
        return 0 <= row < m and 0 <= col < n

    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    seen = set()

    def bfs(row, col):
        queue = deque([(row, col)])
        size = 1
        while len(queue) > 0:
            (row, col) = queue.popleft()
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if is_valid(new_row, new_col) and grid[new_row][new_col] == 1 and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col))
                    size += 1
        return size

    
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and (i, j) not in seen:
                seen.add((i, j))
                result = bfs(i, j)
                ans = max(ans, result)

    return ans

if __name__ == "__main__":
    grid = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    print(max_island_size(grid))