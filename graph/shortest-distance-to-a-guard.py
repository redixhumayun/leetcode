
from collections import deque


def find_shortest_distance_from_a_guard(grid):
    """
    Args:
     grid(list_list_char)
    Returns:
     list_list_int32
    """
    # Write your code here.
    m = len(grid)
    n = len(grid[0])

    def is_valid(row, col):
        return 0 <= row < m and 0 <= col < n

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    
    #   Find the locations of all the guards
    guards_locations = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "G":
                guards_locations.append((i, j))

    #   Add all the guard locations to a queue to start BFS from them
    queue = deque()
    seen = set()
    for location in guards_locations:
        (row, col) = location
        queue.append((row, col, 0))

    while len(queue) > 0:
        (row, col, steps) = queue.popleft()
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if is_valid(new_row, new_col) and\
            (new_row, new_col) not in seen and\
            grid[new_row][new_col] != "W" and\
            grid[new_row][new_col] != "G":
                if grid[new_row][new_col] == "O":
                    grid[new_row][new_col] = steps + 1
                else:
                    grid[new_row][new_col] = min(grid[new_row][new_col], steps + 1)
                seen.add((new_row, new_col))
                queue.append((new_row, new_col, steps + 1))
            

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "W":
                grid[i][j] = -1
            if grid[i][j] == "G":
                grid[i][j] = 0
            if grid[i][j] == "O":
                grid[i][j] = -1
                

    return grid


if __name__ == "__main__":
    grid = [
        ["O", "O", "O", "O", "G"],
        ["O", "W", "W", "O", "O"],
        ["O", "O", "O", "W", "O"],
        ["G", "W", "W", "W", "O"],
        ["O", "O", "O", "O", "G"]
    ]
    print(find_shortest_distance_from_a_guard(grid))

    grid = [["G", "W", "O", "W", "G"]]
    print(find_shortest_distance_from_a_guard(grid))
