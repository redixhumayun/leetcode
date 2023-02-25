from collections import defaultdict
def find_basins(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    visited = set()
    basin_identifier = 'A'
    basins = [row[:] for row in matrix]
    m = len(matrix)
    n = len(matrix[0])

    def is_valid(row, col):
        return 0 <= row < m and 0 <= col < n

    def find_smallest_neighbour(row, col):
        min_value = matrix[row][col]
        min_index = (-1, -1)
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if is_valid(new_row, new_col) and matrix[new_row][new_col] <= min_value:
                min_value = matrix[new_row][new_col]
                min_index = (new_row, new_col)

        return min_index

    def dfs_helper(row, col):
        #   Find the smallest cell surrounding this
        nonlocal basin_identifier, basins
        smallest_neighbour = find_smallest_neighbour(row, col)
        if smallest_neighbour == (-1, -1):
            #   This is a sink
            temp = basin_identifier
            basins[row][col] = temp
            basin_identifier = chr(ord(basin_identifier) + 1)
            return temp
        if smallest_neighbour not in visited:
            visited.add((smallest_neighbour[0], smallest_neighbour[1]))
            basins[row][col] = dfs_helper(smallest_neighbour[0], smallest_neighbour[1])
            return basins[row][col]
        else:
            basins[row][col] = basins[smallest_neighbour[0]][smallest_neighbour[1]]
            return basins[row][col]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i, j) not in visited:
                visited.add((i, j))
                dfs_helper(i, j)
    
    hash_map = defaultdict(int)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            hash_map[basins[i][j]] += 1
    
    output = []
    for key, value in hash_map.items():
        output.append(value)

    output = sorted(output)
    return output


if __name__ == '__main__':
    matrix = [[1, 5, 2], [2, 4, 7], [3, 6, 9]]
    # print(find_basins(matrix))

    matrix = [
        [0, 2, 1, 3],  
        [2, 1, 0, 4],  
        [3, 3, 3, 3],  
        [5, 5, 2, 1]
    ]
    print(find_basins(matrix))