
from collections import defaultdict


def number_of_connected_components(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    #   Build adjacency list using defaultdict from edges
    adj_list = defaultdict(list)
    for edge in edges:
        start, end = edge
        adj_list[start].append(end)
        adj_list[end].append(start)

    stack = []
    seen = set()
    def dfs(node):
        stack.append(node)
        while len(stack) > 0:
            current_node = stack.pop()
            for neighbour in adj_list[current_node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)
    

    components = 0
    for i in range(n):
        if i not in seen:
            seen.add(i)
            components += 1
            dfs(i)
    return components

if __name__ == '__main__':
    print(number_of_connected_components(5, [[0, 1],[1, 2],[0, 2],[3, 4]]))