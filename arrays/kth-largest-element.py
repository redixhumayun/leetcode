from typing import List
from random import randrange

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(left, right, index) -> int:  # type: ignore
            pivot_index = randrange(left, right + 1)
            pivot_element = nums[pivot_index]
            pointer = left

            #   Swap the pivot element with the right element
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            for i in range(left, right):
                if nums[i] <= pivot_element:
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    pointer += 1

            #   Swap the right element and the pointer element
            nums[right], nums[pointer] = nums[pointer], nums[right]
            if pointer == index:
                return nums[pointer]
            if pointer > index:
                return quickselect(left, pointer - 1, index)
            if pointer < index:
                return quickselect(pointer + 1, right, index)
        return quickselect(0, len(nums) - 1, len(nums) - k)

if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))
    print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))