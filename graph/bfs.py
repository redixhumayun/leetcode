from collections import deque, defaultdict

def bfs_traversal(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    #   Build adjacency list from edges list
    adj_list = defaultdict(list)
    for edge in edges:
        start, end = edge
        adj_list[start].append(end)
        adj_list[end].append(start)

    queue = deque()
    seen_list = []
    seen = set()

    def bfs(node):
        queue.append(node)
        while len(queue) > 0:
            current_node = queue.popleft()
            for neighbour in adj_list[current_node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    seen_list.append(neighbour)
                    queue.append(neighbour)

    for i in range(n):
        if i not in seen:
            seen.add(i)
            seen_list.append(i)
            bfs(i)

    return seen_list

if __name__ == '__main__':
    bfs_traversal(6, [[0, 1],[0, 2],[0, 4],[2, 3]])
