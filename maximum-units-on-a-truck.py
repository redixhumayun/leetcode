from functools import cmp_to_key
from typing import List

class Solution:
    def compare(self, item1, item2):
        [i11, i12] = item1
        [i21, i22] = item2
        return i22-i12
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_arr = sorted(boxTypes, key=cmp_to_key(self.compare))
        firstPointer = 0
        ans = 0
        print(sorted_arr)
        while truckSize > 0 and firstPointer < len(sorted_arr):
            element = sorted_arr[firstPointer]
            [boxes, items_per_box] = element
            if boxes >= truckSize:
                ans += truckSize * items_per_box
                truckSize = 0
            else:
                ans += boxes * items_per_box
                truckSize -= boxes
                firstPointer += 1
        return ans
if __name__ == '__main__':
    s = Solution()
    # print(s.maximumUnits([[1,3],[2,2],[3,1]], 4))
    # print(s.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))
    print(s.maximumUnits([[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]], 35))