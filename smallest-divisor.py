import math
from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(divisor):
            total = 0
            for num in nums:
                total += math.ceil(num / divisor)
            return total <= threshold

        left = 1
        right = max(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    s = Solution()
    print(s.smallestDivisor([1,2,5,9], 6))
    print(s.smallestDivisor([2,3,5,7,11], 11))
    print(s.smallestDivisor([19], 5))
    print(s.smallestDivisor([44,22,33,11,1], 5))