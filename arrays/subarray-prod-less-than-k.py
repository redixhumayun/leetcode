class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

if __name__ == "__main__":
    print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))
    print(Solution().numSubarrayProductLessThanK([10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19))