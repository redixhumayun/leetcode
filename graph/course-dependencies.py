from collections import defaultdict

def can_be_completed(n, a, b):
    """
    Args:
     n(int32)
     a(list_int32)
     b(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    adj_list = defaultdict(list)
    for i in range(len(a)):
        adj_list[b[i]].append(a[i])

    arrival = [None] * n
    departure = [None] * n
    timestamp = 1
    seen = set()
    
    def does_cycle_exist(node):
        nonlocal timestamp
        arrival[node] = timestamp
        timestamp += 1
        for neighbour in adj_list[node]:
            if neighbour not in seen:
                seen.add(neighbour)
                if does_cycle_exist(neighbour):
                    return True
            #   check if this node has an arrival but no departure time
            elif arrival[neighbour] != None and departure[neighbour] == None:
                return True
        departure[node] = timestamp
        timestamp += 1
        return False
    
    for i in range(n):
        if i not in seen:
            seen.add(i)
            if does_cycle_exist(i):
                return False
    return True


if __name__ == '__main__':
    n = 4
    a = [1, 1, 3]
    b = [0, 2, 1]
    print(can_be_completed(n, a, b))

    n = 4
    a = [1, 1, 3, 0]
    b = [0, 2, 1, 3]
    print(can_be_completed(n, a, b))