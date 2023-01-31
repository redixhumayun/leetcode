from collections import deque

def minimum_number_of_rolls(n, moves):
    """
    Args:
     n(int32)
     moves(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    def find_min_number_of_moves():
        queue = deque([(0, 0)])
        seen = set()
        while len(queue) > 0:
            current_node, steps = queue.popleft()
            if current_node == n - 1:
                return steps
            for i in range(1, 7):
                new_node = current_node + i
                if new_node >= n:
                    continue
                if moves[new_node] != -1:
                    new_node = moves[new_node]
                if new_node not in seen:
                    seen.add(new_node)
                    queue.append((new_node, steps + 1))
        return -1
    result = find_min_number_of_moves()
    return result

if __name__ == '__main__':
    n = 20
    moves = [-1, 18, -1, -1, -1, -1, -1, -1, 2, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1]
    print(minimum_number_of_rolls(n, moves))

    n = 8
    moves = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    print(minimum_number_of_rolls(n, moves))