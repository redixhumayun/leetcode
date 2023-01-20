from typing import List
from collections import defaultdict, deque

class Solution:
    #   This algorithm uses topological sorting (Kahn's algorithm) to create the list
    #   This algorithm can also be used to detect if a cycle exists in a graph
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #   Create the adj list
        adj_list = defaultdict(list)
        in_degree = defaultdict(int)
        for course, requirement in prerequisites:
            adj_list[requirement].append(course)
            in_degree[course] += 1


        zero_indegree_queue = deque()
        for num in range(numCourses):
            if num not in in_degree:
                zero_indegree_queue.append(num)

        sorted_order = []
        while len(zero_indegree_queue) > 0:
            node = zero_indegree_queue.popleft()
            sorted_order.append(node)
            if node in adj_list:
                for neighbour in adj_list[node]:
                    in_degree[neighbour] -= 1
                    if in_degree[neighbour] == 0:
                        zero_indegree_queue.append(neighbour)

        if len(sorted_order) == numCourses:
            return sorted_order
        return []
        

if __name__ == "__main__":
    print(Solution().findOrder(2, [[1,0]]))
    print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(Solution().findOrder(1, []))
    print(Solution().findOrder(2, [[0, 1], [1, 0]]))