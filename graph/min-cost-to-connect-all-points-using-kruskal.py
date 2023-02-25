from typing import List
import heapq

class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self) -> str:
        return f'({self.point1}, {self.point2}, {self.cost})'

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    def find(self, x):
        if self.root[x] == x:
            return self.root[x]

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distance_list = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x_1, y_1 = points[i]
                x_2, y_2 = points[j]
                distance_from_i = abs(x_1 - x_2) + abs(y_1 - y_2)
                edge = Edge(i, j, distance_from_i)
                distance_list.append(edge)

        heapq.heapify(distance_list)
        uf = UnionFind(len(points))
        total_cost = 0
        count = len(points) - 1
        while len(distance_list) > 0 and count > 0:
            edge = heapq.heappop(distance_list)
            if not uf.connected(edge.point1, edge.point2):
                uf.union(edge.point1, edge.point2)
                total_cost += edge.cost
                count -= 1

        return total_cost
        
        

if __name__ == '__main__':
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(Solution().minCostConnectPoints(points))