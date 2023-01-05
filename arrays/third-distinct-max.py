from typing import List

class Solution:
    def thirdMaxLinearTime(self, nums: List[int]) -> int | float:
        first_max = second_max = third_max = float("-inf")
        for num in nums:
            if num > first_max:
                temp = first_max
                first_max = num
                temp_second = second_max
                second_max = temp
                third_max = temp_second
            elif first_max > num > second_max:
                temp = second_max
                second_max = num
                third_max = temp
            elif second_max > num > third_max:
                third_max = num
        if third_max != float("-inf"):
            return third_max
        return first_max

    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        last_pointer = len(nums) - 1
        max_value = nums[last_pointer]
        temp_max = max_value
        k = 2
        while k > 0 and last_pointer >= 0:
            last_pointer -= 1
            if max_value != nums[last_pointer]:
                max_value = nums[last_pointer]
                k -= 1
        if k > 0 and last_pointer > 0:
            #   Third distinct value not found. Return max value
            return temp_max
        return max_value 

if __name__ == '__main__':
    s = Solution()
    print(s.thirdMaxLinearTime([3, 2, 1]))
    print(s.thirdMaxLinearTime([1, 2]))
    print(s.thirdMaxLinearTime([2, 2, 3, 1]))
    print(s.thirdMaxLinearTime([1, 2, -2147483648]))
    # print(s.thirdMax([1, 2, 2, 5, 3, 5]))
    # print(s.thirdMax([1, 2, -2147483648]))
    # print(s.thirdMax([1, 1, 2]))
    # print(s.thirdMax([1, 2, 2, 5, 3, 5]))
    # print(s.thirdMax([1, 1, 2]))
    # print(s.thirdMax([1, 2, -2147483648]))
    # print(s.thirdMax([1, 2, 2, 5, 3, 5]))
    # print(s.thirdMax([1, 1, 2]))
    # print(s.thirdMax([1, 2, -2147483648]))
    # print(s.thirdMax([1, 2, 2, 5, 3, 5]))
    # print(s.thirdMax([1, 1, 2]))
    # print(s.thirdMax([1, 2, -2147483648]))
    # print(s.thirdMax([1, 2, 2, 5, 3, 5]))
    # print(s.thirdMax([1, 1, 2]))
    # print(s.thirdMax([1, 2, -2147483648]))
    # print(s.thirdMax([1, 2, 2, 5, 3, 5]))
    # print(s.thirdMax([1, 1, 2]))
    # print(s.thirdMax([1, 2, -2147483648]))
    # print(s.thirdMax([1, 2, 2, 5, 3, 5]))
    # print(s.thirdMax([1, 1, 2]))
    # print(s.thirdMax([1, 2, -2147483648]))
    # print(s.thirdMax([1, 2, 2, 5, 3, 5]))