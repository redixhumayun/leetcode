from typing import List
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def calculate_slope(point_1, point_2):
            delta_y = point_1[1] - point_2[1]
            delta_x = point_1[0] - point_2[0]
            try:
                slope = (delta_y / delta_x)
            except ZeroDivisionError:
                slope = float("inf")
            return slope

        def find_points_on_a_line(index, point):
            line_counter = defaultdict(int)
            count = 0
            for j in range(index + 1, len(points)):
                slope = calculate_slope(point, points[j])
                line_counter[slope] += 1
                count = max(line_counter[slope], count)
            return count + 1

        if len(points) < 3:
            return len(points)

        ans = 0
        for index, point in enumerate(points):
            ans = max(ans, find_points_on_a_line(index, point))
        return ans
        

if __name__ == "__main__":
    s = Solution()
    print(s.maxPoints([[1,1],[2,2],[3,3]]))
    print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
    print(s.maxPoints([[0,0],[1,-1],[1,1]]))
    print(s.maxPoints([[-9,-651],[-4,-4],[-8,-582],[9,591],[-3,3]]))
    print(s.maxPoints([[7,3],[19,19],[-16,3],[13,17],[-18,1],[-18,-17],[13,-3],[3,7],[-11,12],[7,19],[19,-12],[20,-18],[-16,-15],[-10,-15],[-16,-18],[-14,-1],[18,10],[-13,8],[7,-5],[-4,-9],[-11,2],[-9,-9],[-5,-16],[10,14],[-3,4],[1,-20],[2,16],[0,14],[-14,5],[15,-11],[3,11],[11,-10],[-1,-7],[16,7],[1,-11],[-8,-3],[1,-6],[19,7],[3,6],[-1,-2],[7,-3],[-6,-8],[7,1],[-15,12],[-17,9],[19,-9],[1,0],[9,-10],[6,20],[-12,-4],[-16,-17],[14,3],[0,-1],[-18,9],[-15,15],[-3,-15],[-5,20],[15,-14],[9,-17],[10,-14],[-7,-11],[14,9],[1,-1],[15,12],[-5,-1],[-17,-5],[15,-2],[-12,11],[19,-18],[8,7],[-5,-3],[-17,-1],[-18,13],[15,-3],[4,18],[-14,-15],[15,8],[-18,-12],[-15,19],[-9,16],[-9,14],[-12,-14],[-2,-20],[-3,-13],[10,-7],[-2,-10],[9,10],[-1,7],[-17,-6],[-15,20],[5,-17],[6,-6],[-11,-8]]))