import heapq
import math
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distanceFromOrigin(x, y):
            return math.sqrt(x**2 + y**2)

        max_heap = []
        for point in points:
            [x, y] = point
            distance = distanceFromOrigin(x, y)
            heapq.heappush(max_heap, (-distance, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        results = []
        for distance, point in max_heap:
            results.append(point)
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.kClosest([[1,3],[-2,2]], 1))
    print(s.kClosest([[3,3],[5,-1],[-2,4]], 3))