from collections import defaultdict, deque

def find_critical_connections(number_of_servers, connections):
    """
    Args:
     number_of_servers(int32)
     connections(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    adj_list = defaultdict(list)
    for start, end in connections:
        adj_list[start].append(end)
        adj_list[end].append(start)

    
    arrival = [0] * number_of_servers
    seen = set()
    lowest = [0] * number_of_servers
    parent = [None] * number_of_servers
    timestamp = 0
    result = []

    def dfs(node):
        nonlocal timestamp
        arrival[node] = timestamp
        lowest[node] = timestamp
        timestamp += 1

        for neighbour in adj_list[node]:
            if neighbour not in seen:
                seen.add(neighbour)
                parent[neighbour] = node
                lowest[node] = min(lowest[node], dfs(neighbour))
            elif neighbour in seen and neighbour != parent[node]:
                lowest[node] = min(arrival[neighbour], lowest[node])

        if lowest[node] == arrival[node] and node != 0:
            result.append([node, parent[node]])
        return lowest[node]
        
    seen.add(0)
    dfs(0)
    if len(result) == 0:
        return [[-1, -1]]
    return result


if __name__ == "__main__":
    number_of_servers = 5
    connections = [
        [0, 1],
        [0, 2],
        [0, 4],
        [1, 2],
        [1, 3]
    ]
    print(find_critical_connections(number_of_servers, connections))

    number_of_servers = 6
    connections = [
        [0, 1],
        [0, 2],
        [1, 2],
        [1, 3],
        [3, 5],
        [3, 4],
        [4, 5]
    ]
    print(find_critical_connections(number_of_servers, connections))