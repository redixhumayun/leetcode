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
    adj_list = defaultdict(list)
    for i in range(len(edge_start)):
        adj_list[edge_start[i]].append(edge_end[i])
        adj_list[edge_end[i]].append(edge_start[i])

    def dfs(node, parent):
        result = True
        for neighbour in adj_list[node]:
            if neighbour not in seen:
                seen.add(neighbour)
                result = dfs(neighbour, node) and result
            elif neighbour in seen and neighbour != parent:
                return False
        return result


    seen = set()
    components = 0
    result = True
    for i in range(node_count):
        if i not in seen:
            seen.add(i)
            components += 1
            result = dfs(i, None) and result

    if components > 1:
        return False
    
    return result

if __name__ == '__main__':
    print(is_it_a_tree(4, [0, 0, 0], [1, 2, 3]))
    print(is_it_a_tree(4, [0, 0, 1, 2], [3, 1, 2, 0]))