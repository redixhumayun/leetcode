from collections import defaultdict, deque

def find_longest_path(dag_nodes, dag_from, dag_to, dag_weight, from_node, to_node):
    """
    Args:
     dag_nodes(int32)
     dag_from(list_int32)
     dag_to(list_int32)
     dag_weight(list_int32)
     from_node(int32)
     to_node(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    adj_list = defaultdict(list)
    for index in range(len(dag_from)):
        adj_list[dag_from[index]].append((dag_to[index], dag_weight[index]))

    def topological_sort():
        #   This algorithm uses Kahn's algorithm (Topological Sorting) to find the longest path
        #   This will run in O(V+E) time
        indegrees = [0] * (dag_nodes + 1)
        for index, value in enumerate(dag_to):
            indegrees[value] += 1

        nodes_with_no_incoming_edges = deque()
        for index, value in enumerate(indegrees):
            if value == 0:
                nodes_with_no_incoming_edges.append(index)

        topological_ordering = []

        while len(nodes_with_no_incoming_edges) > 0:
            current_node = nodes_with_no_incoming_edges.popleft()
            topological_ordering.append(current_node)

            for neighbour, _ in adj_list[current_node]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour] == 0:
                    nodes_with_no_incoming_edges.append(neighbour)
    
        return topological_ordering

    top_order = topological_sort()
    top_order = top_order[1:]
    
    dist = [float("-inf")] * (dag_nodes + 1)
    path = [[]] * (dag_nodes + 1)
    path[from_node] = [from_node]
    dist[from_node] = 0

    for i in top_order:
        current_path = path[i][:]
        node = i
        for neighbour, weight in adj_list[node]:
            new_distance = dist[node] + weight
            if new_distance > dist[neighbour]:
                dist[neighbour] = max(dist[neighbour], new_distance)
                current_path.append(neighbour)
                path[neighbour] = current_path[:]
                current_path.pop()

    return path[to_node]

    #   This algorithm uses DFS to find the longest path
    #   Since DFS requires every path between start & end to be explicitly traversed, it could lead to an
    #   exponential time algorithm
    # ans = 0
    # result = []
    # def dfs(node, node_list, path_sum):
    #     nonlocal ans, result
    #     if node == to_node:
    #         ans = max(ans, path_sum)
    #         if ans == path_sum:
    #             result = node_list[:]
    #         return
    #     for neighbour, weight in adj_list[node]:
    #         node_list.append(neighbour)
    #         dfs(neighbour, node_list, path_sum + weight)
    #         node_list.pop()

    # dfs(from_node, [from_node], 0)
    # return result


if __name__ == "__main__":
    dag_nodes = 4
    dag_from = [1, 1, 1, 3]
    dag_to = [2, 3, 4, 4]
    dag_weight = [2, 2, 4, 3]
    from_node = 1
    to_node = 4
    print(find_longest_path(dag_nodes, dag_from, dag_to, dag_weight, from_node, to_node))

    dag_nodes = 3
    dag_from = [2, 2, 3]
    dag_to = [1, 3, 1]
    dag_weight = [4, 1, 2]
    from_node = 2
    to_node = 1
    print(find_longest_path(dag_nodes, dag_from, dag_to, dag_weight, from_node, to_node))