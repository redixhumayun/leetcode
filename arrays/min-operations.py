from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = 0
        right = len(nums) - 1
        operations = 0
        while left <= right and x > 0:
            #   Remove the larger of the two values but bounded by the value of x
            value_to_remove = None
            if nums[left] <= nums[right] and nums[right] <= x:
                value_to_remove = nums[right]
                right -= 1
                operations += 1
                x -= value_to_remove
            elif nums[left] > nums[right] and nums[left] <= x:
                value_to_remove = nums[left]
                left += 1
                operations += 1
                x -= value_to_remove
            else:
                #   Could not remove either value
                #   Try to remove whatever value is smaller than x
                if nums[left] <= x:
                    x = x - nums[left]
                    left += 1
                    operations += 1
                    continue
                if nums[right] <= x:
                    x = x - nums[right]
                    right -= 1
                    operations += 1
                    continue
                return -1
        if x == 0:
            return operations
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.minOperations([1, 1, 4, 2, 3], 5))
    print(solution.minOperations([5, 6, 7, 8, 9], 4))
    print(solution.minOperations([3, 2, 20, 1, 1, 3], 10))
    print(solution.minOperations([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365))