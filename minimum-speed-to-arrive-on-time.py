import math
from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1

        def checkArrival(speed):
            total = 0
            for i in range(len(dist) - 1):
                total +=  math.ceil(dist[i] / speed)
            total += (dist[-1] / speed)
            return total <= hour

        left = 1
        right = 10 ** 7
        while left <= right:
            mid = (left + right) // 2
            if checkArrival(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    s = Solution()
    # print(s.minSpeedOnTime([1,3,2], 6))
    # print(s.minSpeedOnTime([1,3,2], 2.7))
    # print(s.minSpeedOnTime([1,3,2], 1.9))
    print(s.minSpeedOnTime([1,1,100000], 2.01))
    # print(s.minSpeedOnTime([1,1,100000], 2.01))
    # print(s.minSpeedOnTime([1,1,100000], 2.02))
    # print(s.minSpeedOnTime([1,1,100000], 2.03))
    # print(s.minSpeedOnTime([1,1,100000], 2.04))
    # print(s.minSpeedOnTime([1,1,100000], 2.05))
    # print(s.minSpeedOnTime([1,1,100000], 2.06))
    # print(s.minSpeedOnTime([1,1,100000], 2.07))
    # print(s.minSpeedOnTime([1,1,100000], 2.08))
    # print(s.minSpeedOnTime([1,1,100000], 2.09))
    # print(s.minSpeedOnTime([1,1,100000], 2.1))
    # print(s.minSpeedOnTime([1,1,100000], 2.11))
    # print(s.minSpeedOnTime([1,1,100000], 2.12))
    # print(s.minSpeedOnTime([1,1,100000], 2.13))
    # print(s.minSpeedOnTime([1,1,100000], 2.14))
    # print(s.minSpeedOnTime([1,1,100000], 2.15))
    # print(s.minSpeedOnTime([1,1,100000], 2.16))
    # print(s.minSpeedOnTime([1,1,100000], 2.17))
    # print(s.minSpeedOnTime([1,1,100000], 2.18))
    # print(s.minSpeedOnTime([1,1,100000], 2.19))
    # print(s.minSpeedOnTime([1,1,100000], 2.2))
    # print(s.minSpeedOnTime([1,1,100000], 2.21))