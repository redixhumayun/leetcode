from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(max_sum):
            total = 0
            subarray_count = 0
            for num in nums:
                total += num
                if total > max_sum:
                    total = num
                    subarray_count += 1
            return subarray_count + 1   #   Add 1 to count the last array which hasn't split
        
        #   Solution space
        left = max(nums)
        right = sum(nums)

        ans = 0

        while left <= right:
            mid = (left + right) // 2
            subarray_count = check(mid)
            if subarray_count <= k:
                #   The mid value is too large, not able to get enough subarrays or can get enough subarrays, so try smaller values
                #   Remove right side of solution space
                right = mid - 1
                ans = mid
            elif subarray_count > k:
                #   The mid value is too small, can get more arrays than required
                #   Remove left side of solution space
                left = mid + 1
        return ans

if __name__ == "__main__":
    print(Solution().splitArray([7, 2, 5, 10, 8], 2))
    print(Solution().splitArray([1, 2, 3, 4, 5], 2))
    print(Solution().splitArray([10,5,13,4,8,4,5,11,14,9,16,10,20,8], 8))