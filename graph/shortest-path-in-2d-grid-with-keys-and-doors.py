from collections import deque

def find_shortest_path(grid):
    """
    Args:
     grid(list_str)
    Returns:
     list_list_int32
    """
    # Write your code here.
    #   First find all the keys / doors that need to be visited
    doors_to_be_visited = set()
    start_index = (0, 0)
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    m = len(grid)
    n = len(grid[0])

    def is_valid(row, col):
        return 0 <= row < m and 0 <= col < n

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            char = grid[i][j]
            if 65 <= ord(char) <= 90:
                doors_to_be_visited.add(char)
            if char == "@":
                start_index = (i, j)

    queue = deque([(start_index[0], start_index[1], tuple(), tuple(), [])])
    visited = set()
    def bfs():
        while len(queue) > 0:
            (row, col, keys_tuple, doors_tuple, path) = queue.popleft()
            path.append([row, col])
            print(path)
            current_character = grid[row][col]

            if 97 <= ord(current_character) <= 122:
                #   This char is a key
                if current_character not in keys_tuple:
                    keys_tuple = (*keys_tuple, current_character)

            if 65 <= ord(current_character) <= 90:
                #   This current_character is a door
                #   Can only visit if key is obtained
                if chr(ord(current_character) + 32) in keys_tuple and current_character not in doors_tuple:
                    doors_tuple = (*doors_tuple, current_character)

            if current_character == "+":
                #   Reached the end but can only complete when all keys are collected and
                #   all doors visited
                if len(keys_tuple) == len(doors_tuple) == len(doors_to_be_visited):
                    return path
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if is_valid(new_row, new_col) and (new_row, new_col, keys_tuple, doors_tuple) not in visited and\
                    grid[new_row][new_col] != "#":
                    visited.add((new_row, new_col, keys_tuple, doors_tuple))
                    queue.append((new_row, new_col, keys_tuple, doors_tuple, path[:]))
        return -1
    return bfs()


if __name__ == '__main__':
    grid = [
        "...B",
        ".b#.",
        "@#+."
    ]
    # print(find_shortest_path(grid))

    grid = [
        "#########",
        "#b.A.@.a#",
        "#########",
    ]
    # print(find_shortest_path(grid))

    grid = [
        "...B",
        ".b#.",
        "@#+.",
        "a.#.",
        "#..A"
    ]
    print(find_shortest_path(grid))

    # grid = [
    #     "########################",
    #     "#@..............ac.GI.b#",
    #     "###d#e#f################",
    #     "###A#B#C################",
    #     "###g#h#i################",
    #     "########################",
    # ]
    # print(find_shortest_path(grid))

    # grid = [
    #     "#################",
    #     "#i.G..c...e..H.p#",
    #     "########.########",
    #     "#j.A..b...f..D.o#",
    #     "########@########",
    #     "#k.E..a...g..B.n#",
    #     "########.########",
    #     "#l.F..d...h..C.m#",
    #     "#################",
    # ]
    # print(find_shortest_path(grid))

    # grid = [
    #     "########################",
    #     "#@..............ac.GI.b#",
    #     "###d#e#f################",
    #     "###A#B#C################",
    #     "###g#h#i################",
    #     "########################",
    # ]
    # print(find_shortest_path(grid))

    # grid = [
    #     "#################",
    #     "#i.G..c...e..H.p#",
    #     "########.########",
    #     "#j.A..b...f..D.o#",
    #     "########@########",
    #     "#k.E..a...g..B.n#",
    #     "########.########",
    #     "#l.F..d...h..C.m#",
    #     "#################",
    # ]
    # print(find_shortest_path(grid))