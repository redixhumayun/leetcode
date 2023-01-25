from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        def two_sum_less(left, right, target):
            def binary_search(left, right, target):
                while left < right:
                    mid_point = (left + right) // 2
                    if nums[mid_point] == target:
                        return mid_point
                    if nums[mid_point] < target:
                        left = mid_point + 1
                    else:
                        right = mid_point - 1
                return left

            count = 0
            for index in range(left, right - 1):
                num = nums[index]
                x = target - num
                insertion_point = binary_search(index + 1, right, x)
                if insertion_point < len(nums) and nums[insertion_point] == x:
                    insertion_point -= 1
                
                if insertion_point <= left:
                    count += 0
                else:
                    count += insertion_point - index
            return count

        result = 0
        for index in range(len(nums) - 2):
            num = nums[index]
            x = target - num
            number_of_elems = two_sum_less(index + 1, len(nums) - 1, x)
            result += number_of_elems

        return result


        
if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumSmaller([-2,0,1,3], 2))
    # print(solution.threeSumSmaller([-2,0,1,3], 0))
    # print(solution.threeSumSmaller([-2,0,1,3], 1))
    # print(solution.threeSumSmaller([-2,0,1,3], 4))