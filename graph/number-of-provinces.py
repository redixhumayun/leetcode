from collections import defaultdict
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        class UnionFind:
            def __init__(self):
                self.root = [i for i in range(n)]
                self.rank = [1] * n
                self.components = n

            def find(self, x):
                if self.root[x] == x:
                    return self.root[x]
                root = self.find(self.root[x])
                self.root[x] = root
                return self.root[x]

            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)
                if root_x != root_y:
                    if self.rank[root_x] > self.rank[root_y]:
                        self.root[root_y] = root_x
                    elif self.rank[root_y] > self.rank[root_x]:
                        self.root[root_x] = root_y
                    else:
                        self.root[root_y] = root_x
                        self.rank[root_x] += 1
                    self.components -= 1

        uf = UnionFind()
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        return uf.components             


if __name__ == "__main__":
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(Solution().findCircleNum(isConnected))

    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print(Solution().findCircleNum(isConnected))