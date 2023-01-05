from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        def binary_search():
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                if nums[mid] > target:
                    right = mid - 1
            return -1
        result = binary_search()
        if result == -1:
            return [-1, -1]
        left_pointer = right_pointer = result
        while left_pointer > -1:
            if nums[left_pointer] == nums[result]:
                left_pointer -= 1
            else:
                break
        while right_pointer < len(nums):
            if nums[right_pointer] == nums[result]:
                right_pointer += 1
            else:
                break
        return [left_pointer + 1, right_pointer - 1]

if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
    print(Solution().searchRange([], 0))
    print(Solution().searchRange([1], 1))
    print(Solution().searchRange([1, 4], 4))
    print(Solution().searchRange([3,3,3], 3))