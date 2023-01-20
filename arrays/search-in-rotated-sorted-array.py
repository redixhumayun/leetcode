from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            #   Find which side is continuous and therefore sorted
            if nums[left] < nums[mid]:
                #   Left hand side is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                #   Right hand side is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1         
        return -1

if __name__ == "__main__":
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
    print(Solution().search([1], 0))
    print(Solution().search([7, 0, 1, 2, 4, 5, 6], 0))
    print(Solution().search([3, 1], 1))