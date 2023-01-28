from collections import deque

def count_islands(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    m = len(matrix)
    n = len(matrix[0])
    def is_valid(row, col):
        return 0 <= row < m and 0 <= col < n

    directions = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))
    seen = set()

    def bfs(row, col):
        queue = deque([(row, col)])
        while len(queue) > 0:
            row, col = queue.popleft()
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if is_valid(new_row, new_col) and matrix[new_row][new_col] == 1 and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col))

    islands = 0
    for i in range(m):
        for j in range(n):
            if (i, j) not in seen and matrix[i][j] == 1:
                seen.add((i, j))
                bfs(i, j)
                islands += 1

    return islands


if __name__ == "__main__":
    matrix = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]
    print(count_islands(matrix))