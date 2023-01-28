from collections import defaultdict

def check_if_eulerian_path_exists(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     bool
    """
    # Write your code here.
    #   Eulerian cycle can exist iff there are either 0 or 2 vertices with an odd degree
    counter = defaultdict(int)
    for edge in edges:
        from_node, to_node = edge
        counter[from_node] += 1
        counter[to_node] += 1

    odd_vertices_count = 0
    for key, value in counter.items():
        if value % 2 != 0:
            odd_vertices_count += 1
    
    if odd_vertices_count == 0 or odd_vertices_count == 2:
        return True
    return False


if __name__ == '__main__':
    n = 4
    edges = [[0, 1],[1, 2],[1, 3],[2, 0],[3, 2]]
    print(check_if_eulerian_path_exists(n, edges))