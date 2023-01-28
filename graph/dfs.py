
from collections import defaultdict


def dfs_traversal(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    #   Build adjacency list using a defaultdict from the edges list
    adj_list = defaultdict(list)
    for edge in edges:
        start, end = edge
        adj_list[start].append(end)
        adj_list[end].append(start)

    #   Iterative implementation
    stack = []
    seen = set()
    output_list = []
    parent = [None] * n
    arrival = [None] * n
    departure = [None] * n
    timestamp = 0

    def dfs_recursive(node):
        nonlocal timestamp
        arrival[node] = timestamp
        timestamp += 1
        
        for neighbour in adj_list[node]:
            if neighbour not in seen:
                seen.add(neighbour)
                parent[neighbour] = node
                output_list.append(neighbour)
                dfs_recursive(neighbour)
        departure[node] = timestamp
        timestamp += 1
 
    def dfs_iterative(node):
        stack.append(node)
        while len(stack) > 0:
            current_node = stack.pop()
            for neighbour in adj_list[current_node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    output_list.append(neighbour)
                    stack.append(neighbour)

    for i in range(n):
        if i not in seen:
            seen.add(i)
            output_list.append(i)
            dfs_recursive(i)
            # dfs_iterative(i)

    print(parent, arrival, departure)
    return output_list

if __name__ == '__main__':
    print(dfs_traversal(6, [[0, 1],[0, 2],[1, 4],[3, 5]]))
