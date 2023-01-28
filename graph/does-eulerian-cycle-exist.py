from collections import defaultdict

def check_if_eulerian_cycle_exists(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     bool
    """
    # Write your code here.
    #   An eulerian cycle can occur in an undirected graph iff all nodes have an even degree
    #   Count the degree of each node and see if any nodes have an odd degree
    counter = defaultdict(int)
    for edge in edges:
        from_node, to_node = edge
        counter[from_node] += 1
        counter[to_node] += 1

    for key, value in counter.items():
        if value % 2 != 0:
            return False
    return True


if __name__ == '__main__':
    print(check_if_eulerian_cycle_exists(4, [[0, 1],[0, 2],[1, 3],[3, 0],[3, 2],[4, 3],[4, 0]]))
    print(check_if_eulerian_cycle_exists(6, [[0, 4],
[0, 5],
[1, 2],
[2, 3],
[3, 1],
[4, 3]]))