from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = 0
        for num in nums:
            mask = mask ^ num

        return mask
if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2,2,1]))
    print(s.singleNumber([4,1,2,1,2]))