from collections import deque


def zombie_cluster(zombies):
    """
    Args:
     zombies(list_str)
    Returns:
     int32
    """
    # Write your code here.
    n = len(zombies)

    def is_valid(row, col):
        return 0 <= row < n and 0 <= col < n

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    def bfs(row, col):
        queue = deque([(row, col)])
        while len(queue) > 0:
            (row, col) = queue.popleft()
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if is_valid(new_row, new_col) and zombies[new_row][new_col] == "1"\
                and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col))


    seen = set()
    clusters = 0
    for i in range(n):
        if (i, i) not in seen:
            clusters += 1
            seen.add((i, i))
            bfs(i, i)

    return clusters

if __name__ == "__main__":
    zombies = ["1100", "1110", "0110", "0001"]
    print(zombie_cluster(zombies))

    zombies = ["10000","01000","00100","00010","00001"]
    print(zombie_cluster(zombies))