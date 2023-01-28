from collections import deque, defaultdict

def course_schedule(n, prerequisites):
    """
    Args:
     n(int32)
     prerequisites(list_list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    adj_list = defaultdict(list)
    for dependent, independent in prerequisites:
        adj_list[independent].append(dependent)

    def topological_sort():
        indegrees = [0] * (n)
        for dependent, independent in prerequisites:
            indegrees[dependent] += 1

        seen = set()
        nodes_with_zero_indegree = deque()
        for index, value in enumerate(indegrees):
            if value == 0:
                nodes_with_zero_indegree.append(index)
                seen.add(index)

        top_order = []
        while len(nodes_with_zero_indegree) > 0:
            current_node = nodes_with_zero_indegree.popleft()
            top_order.append(current_node)
            for neighbour in adj_list[current_node]:
                if neighbour not in seen:
                    indegrees[neighbour] -= 1
                    if indegrees[neighbour] == 0:
                        seen.add(neighbour)
                        nodes_with_zero_indegree.append(neighbour)
        return top_order
        
    course_order = topological_sort()
    if len(course_order) < n-1:
        return ["-1"]
    return course_order

if __name__ == "__main__":
    n = 4
    prerequisites = [
        [1, 0],
        [2, 0],
        [3, 1],
        [3, 2]
    ]
    print(course_schedule(n, prerequisites))