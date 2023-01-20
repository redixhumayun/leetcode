from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        #   Build adjacency list
        adj_list = defaultdict(list)
        for route in routes:
            for index in range(len(route) - 1):
                adj_list[route[index]].append(route[index + 1])
            adj_list[route[-1]].append(route[0])

        #   Build route index hashmap
        route_index_hash_map = defaultdict(list)
        for index, route in enumerate(routes):
            for stop in route:
                route_index_hash_map[stop].append(index)

        print(route_index_hash_map)

        queue = deque([])

        #   The iterable displays (current_stop, current_route, bus_count)
        route_index = route_index_hash_map[source]
        for r in route_index:
            queue.append((source, r, 0))

        seen = set()
        while len(queue) > 0:
            (current_stop, current_route, bus_count) = queue.popleft()
            if current_stop == target:
                return bus_count
            for neighbour in adj_list[current_stop]:
                route_index_list = route_index_hash_map[neighbour]
                for r in route_index_list:
                    if r != current_route:
                        bus_count += 1
                    queue.append((neighbour, r, bus_count))
                    bus_count -= 1
            

        # seen = set()
        # count = 0
        # destination_flag = False
        # def dfs(node):
        #     nonlocal count, destination_flag
        #     if node == target:
        #         #   The destination was found. Set the flag and increment the bus count
        #         destination_flag = True
        #         count += 1
        #         return
        #     for neighbour in adj_list[node]:
        #         if neighbour not in seen:
        #             seen.add(neighbour)
        #             dfs(neighbour)
        #         else:
        #             #   A cycle has been detected if a node that was previously found is seen again
        #             #   This implies that the route for a bus was taken completely
        #             count += 1

        # #   The bus route has to start from source
        # seen.add(source)
        # dfs(source)
        # if destination_flag:
        #     return count
        # return -1

if __name__ == "__main__":
    # routes = [[1,2,7],[3,6,7]]
    # source = 1
    # target = 6
    # print(Solution().numBusesToDestination(routes, source, target))

    # routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
    # source = 15
    # target = 12
    # print(Solution().numBusesToDestination(routes, source, target))

    routes = [[24],[3,6,11,14,22],[1,23,24],[0,6,14],[1,3,8,11,20]]
    source = 20
    target = 8
    print(Solution().numBusesToDestination(routes, source, target))