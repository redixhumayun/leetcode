from collections import defaultdict

def is_it_a_tree(node_count, edge_start, edge_end):
    """
    Args:
     node_count(int32)
     edge_start(list_int32)
     edge_end(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    #   Build adjacency list
    adj_list = defaultdict(list)
    for start, end in zip(edge_start, edge_end):
        adj_list[start].append(end)
        adj_list[end].append(start)

    visited = set()
    parents = [-1 for i in range(node_count)]
    def does_cycle_exist(node):
        for neighbour in adj_list[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                parents[neighbour] = node
                if does_cycle_exist(neighbour):
                    return True
            elif parents[node] != neighbour:
                #   if the neighbour is not the parent
                return True
        return False
    
    components = 0
    cycle = False
    for i in range(node_count):
        if i not in visited:
            components += 1
            visited.add(i)
            cycle = does_cycle_exist(i)
    
    if cycle or components > 1:
        return False
    return True


if __name__ == "__main__":
    node_count = 4
    edge_start = [0, 0, 0]
    edge_end = [1, 2, 3]
    print(is_it_a_tree(node_count, edge_start, edge_end))

    node_count = 4
    edge_start = [0, 0, 1, 2]
    edge_end = [3, 1, 2, 0]
    print(is_it_a_tree(node_count, edge_start, edge_end))