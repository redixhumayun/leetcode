from collections import deque

def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    """
    Args:
     rows(int32)
     cols(int32)
     start_row(int32)
     start_col(int32)
     end_row(int32)
     end_col(int32)
    Returns:
     int32
    """
    # Write your code here.
    def is_valid(row, col):
        return 0 <= row < rows and 0 <= col < cols

    directions = ((2, 1), (-2, 1), (1, 2), (-1, 2), (2, -1), (-2, -1), (1, -2), (-1, -2))
    queue = deque([(start_row, start_col, 0)])
    seen = {(start_row, start_col)}

    while len(queue) > 0:
        (row, col, level) = queue.popleft()

        if (row, col) == (end_row, end_col):
            return level

        for i in (-1, 1):
            for dx, dy in directions:
                new_row = new_col = -1
                if i == -1:
                    new_row, new_col = row + dx, col + dy
                else:
                    new_row, new_col = row + dy, col + dx

                if is_valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col, level + 1))

    return -1


if __name__ == '__main__':
    print(find_minimum_number_of_moves(5, 5, 0, 0, 4, 1))