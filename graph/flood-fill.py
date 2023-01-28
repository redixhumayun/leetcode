from collections import deque

def flood_fill(pixel_row, pixel_column, new_color, image):
    """
    Args:
     pixel_row(int32)
     pixel_column(int32)
     new_color(int32)
     image(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    queue = deque([(pixel_row, pixel_column)])
    seen = set()
    seen.add((pixel_row, pixel_column))
    color_to_look_for = image[pixel_row][pixel_column]

    def is_valid(row, col):
        return 0 <= row < len(image) and 0 <= col < len(image[0])

    while len(queue) > 0:
        (row, col) = queue.popleft()
        if image[row][col] != color_to_look_for:
            continue

        image[row][col] = new_color

        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if is_valid(new_row, new_col) \
            and (new_row, new_col) not in seen \
            and image[new_row][new_col] == color_to_look_for:
                seen.add((new_row, new_col))
                queue.append((new_row, new_col))
            
    return image


if __name__ == '__main__':
    print(flood_fill(0, 1, 2, [[0, 1, 3],[1, 1, 1],[1, 5, 4]]))
    # print(flood_fill(1, 1, 2, [[0,0,0],[0,1,1]]))