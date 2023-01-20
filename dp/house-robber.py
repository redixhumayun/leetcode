from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        #   Bottom up iterative approach
        arr = [0] * (len(nums) + 1)

        N = len(nums)
        arr[N] = 0
        arr[N-1] = nums[-1]

        for i in range(N-2, -1, -1):
            arr[i] = max(arr[i+1], arr[i+2] + nums[i])

        return arr[0]


        #   Top down recursive solution
        # memo = {}
        # def dp(index):
        #     if index >= len(nums):
        #         return 0
        #     if index in memo:
        #         return memo[index]
        #     skip_current_house = dp(index + 1)
        #     rob_current_house = dp(index + 2) + nums[index]
        #     ans = max(rob_current_house, skip_current_house)
        #     memo[index] = ans
        #     return ans
        # return dp(0)
        
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([1, 2, 3, 1]))
    print(solution.rob([1, 7, 5, 4, 2, 8, 6, 1, 11]))
    print(solution.rob([2, 7, 9, 3, 1]))
    print(solution.rob([2, 1, 1, 2]))