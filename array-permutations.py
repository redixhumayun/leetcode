from typing import List

class Solution:
    #   This solution iterates over the entire array each time and for each iteration, check if the num needs to be added
    def permute_leetcode(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
        
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
            
        ans = []
        backtrack([])
        return ans

    #   Using the methodology of popping the first value off and then adding it back on the end after permutations have been generated
    def permute_pop(self, nums):
        results = []
        #   Base case
        if len(nums) == 1:
            return [nums[:]]
        for num in nums:
            value = nums.pop(0)
            perms = self.permute_pop(nums)

            for perm in perms:
                perm.append(value)
            results.extend(perms)
            nums.append(value)
        return results

    #   Using the methodology of holding one element constant while others are changed
    def permute_constant(self, nums):
        results = []
        if len(nums) == 1:
            #   Base case
            return [nums]

        for i in range(len(nums)):
            constant_number = nums[i]   #   For this iteration, this number will be held constant
            first = nums[:i]
            last = nums[i+1:]
            perms = self.permute_constant(first + last)
            for perm in perms:
                r = [constant_number, *perm]
                results.append(r)
        return results

    
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permute_leetcode(nums)

if __name__ == "__main__":
    s = Solution()
    print(s.permute([1,2,3]))