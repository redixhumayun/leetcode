from collections import defaultdict

def has_cycle(number_of_vertices, number_of_edges, edges):
    """
    Args:
     number_of_vertices(int32)
     number_of_edges(int32)
     edges(list_list_int32)
    Returns:
     bool
    """
    # Write your code here.
    #   Build adjacency list
    adj_list = defaultdict(list)
    for from_node, to_node in edges:
        adj_list[from_node].append(to_node)

    seen = set()

    def dfs(node, node_list):
        result = False
        for neighbour in adj_list[node]:
            if neighbour in node_list:
                return True
            if neighbour not in seen:
                seen.add(neighbour)
                node_list.append(neighbour)
                result = dfs(neighbour, node_list) or result
                node_list.pop()
        return result

    for i in range(number_of_vertices):
        if i not in seen:
            seen.add(i)
            result = dfs(i, [i])
            if result is True:
                return True

    return False


if __name__ == "__main__":
    number_of_vertices = 5
    number_of_edges = 7
    edges = [
        [0, 1],
        [0, 3],
        [1, 3],
        [1, 2],
        [2, 3],
        [4, 0],
        [2, 4]
    ]
    print(has_cycle(number_of_vertices, number_of_edges, edges))