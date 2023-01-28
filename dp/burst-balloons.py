from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        def dp(i, j) -> int:
            if i > j:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            #   Pop each balloon one at a time
            ans = 0
            for k in range(i, j+1):
                #   Pop the kth balloon last but store the value in gain
                gain = nums[i-1] * nums[k] * nums[j+1]

                #   Check the left subarray and right subarray recursively
                left_chain = dp(i, k-1)
                right_chain = dp(k+1, j)
                ans = max(ans, left_chain + gain + right_chain)
            memo[(i, j)] = ans
            return memo[(i, j)]
        nums = [1] + nums + [1]
        return dp(1, len(nums) - 2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxCoins([3, 1, 5, 8]))