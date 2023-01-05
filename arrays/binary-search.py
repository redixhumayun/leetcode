from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beginPointer = 0
        endPointer = len(nums) - 1
        while beginPointer <= endPointer:
            midPointer = (beginPointer + endPointer) // 2
            if nums[midPointer] == target:
                return midPointer
            if nums[midPointer] > target:
                endPointer = midPointer - 1
            elif nums[midPointer] < target:
                beginPointer = midPointer + 1
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.search([-1,0,3,5,9,12], 9))

    print(s.search([2], 1))