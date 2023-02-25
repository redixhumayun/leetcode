from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #   First build the adjacency list for the directed graph
        size = n
        adj_list = defaultdict(list)
        for (start, stop, cost) in flights:
            adj_list[start].append((stop, cost))

        visited = [-1] * size
        priority_queue = []
        distance = [float("inf")] * size
        heapq.heapify(priority_queue)

        visited[src] = 1
        distance[src] = 0

        hops = [-1] * size
        hops[0] = 0

        for ngh, cost in adj_list[src]:
            heapq.heappush(priority_queue, (ngh, cost, 1))
            hops[ngh] = 1

        while len(priority_queue) > 0:
            node, cost, number_of_hops = heapq.heappop(priority_queue)
            
            if node == dst:
                return cost

            if visited[node] == -1:
                visited[node] = 1
                distance[node] = cost

                for neighbour, weight in adj_list[node]:
                    if visited[neighbour] == -1:
                        #   Only add the neighbour if reaching the neighbour requires less than k edges
                        if neighbour != dst and number_of_hops + 1 <= k:
                            heapq.heappush(priority_queue, (neighbour, cost + weight, number_of_hops + 1))
                        elif neighbour == dst and number_of_hops + 1 <= k+1:
                            heapq.heappush(priority_queue, (neighbour, cost + weight, number_of_hops + 1))

        return -1

if __name__ == '__main__':
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 2
    print(Solution().findCheapestPrice(n, flights, src, dst, k))

    n = 4
    flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
    src = 0
    dst = 3
    k = 1
    print(Solution().findCheapestPrice(n, flights, src, dst, k))