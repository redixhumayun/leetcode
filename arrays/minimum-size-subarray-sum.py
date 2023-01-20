from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = nums[left]
        min_length = float("inf")

        if sum >= target:
            return 1

        for right in range(1, len(nums)):
            sum += nums[right]
            while sum >= target and left <= right:
                min_length = min(min_length, right - left + 1)
                sum -= nums[left]
                left += 1
                

        if min_length == float("inf"):
            return 0
        return min_length

if __name__ == '__main__':
    solution = Solution()
    print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(solution.minSubArrayLen(4, [1, 4, 4]))