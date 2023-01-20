from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        queue = deque()
        visited = set()

        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n

        #   Start a BFS from top and left
        for i in range(n):
            queue.append((0, i))
            visited.add((0, i))

        for i in range(m):
            queue.append((i, 0))
            visited.add((i, 0))

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while len(queue) > 0:
            (row, col) = queue.popleft()
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if is_valid(new_row, new_col) and \
                heights[row][col] <= heights[new_row][new_col] and \
                (new_row, new_col) not in visited:
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))

        pacific_set = visited.copy()
        visited.clear()

        #   Start a BFS from bottom and right
        for i in range(n):
            queue.append((n - 1, i))
            visited.add((n - 1, i))

        for i in range(m):
            queue.append((i, m - 1))
            visited.add((i, m - 1))

        while len(queue) > 0:
            (row, col) = queue.popleft()
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if is_valid(new_row, new_col) and \
                heights[row][col] <= heights[new_row][new_col] and \
                (new_row, new_col) not in visited:
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))

        atlantic_set = visited.copy()
        visited.clear()

        #   Find intersection of the two sets
        result = list(pacific_set.intersection(atlantic_set))
        output = []
        for r in result:
            output.append(list(r))

        return output

if __name__ == "__main__":
    print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    print(Solution().pacificAtlantic([[1]]))
    print(Solution().pacificAtlantic([[1,1],[1,1],[1,1]]))
    # print(Solution().pacificAtlantic([[1,2,3],[8,9,4],[7,6,5]]))
    # print(Solution().pacificAtlantic([[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]))
    # print(Solution().pacificAtlantic([[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],[16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]]))  
