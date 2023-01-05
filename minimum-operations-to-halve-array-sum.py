import heapq

class Solution:
    def halveArray(self, nums) -> int:
        nums_sum = sum(nums)
        nums = [-num for num in nums]
        heapq.heapify(nums)
        heap_sum = nums_sum
        ops = 0
        #   Every time the largest number is halved, subtract the difference from heap_sum
        while heap_sum > nums_sum / 2:
            largest = abs(heapq.heappop(nums))
            reduced_largest = largest / 2
            diff = abs(largest - reduced_largest)
            heap_sum -= diff
            ops += 1
            heapq.heappush(nums, -reduced_largest)
        return ops

if __name__ == '__main__':
    nums = [5,19,8,1]
    print(Solution().halveArray(nums))