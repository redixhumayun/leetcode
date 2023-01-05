from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort() #   O(n.log(n)) operation
        count = 0
        firstPointer = secondPointer = 0
        while secondPointer < len(nums):
            if nums[secondPointer] - nums[firstPointer] > k:
                #   Found a subsequence, it is from firstPointer to secondPointer - 1 at this point
                count += 1
                firstPointer = secondPointer
            else:
                #   Keep incrementing second pointer until the subsequence is found
                secondPointer += 1
        return count + 1

if __name__ == '__main__':
    s = Solution()
    # print(s.partitionArray([3,6,1,2,5], 2))
    # print(s.partitionArray([1, 2, 3], 1))
    print(s.partitionArray([2, 2, 4, 5], 0))
    # print(s.partitionArray([7, 5, 8, 9, 2, 8, 3, 1], 3))
    # print(s.partitionArray([1, 2, 3, 4, 5], 3))
    # print(s.partitionArray([1, 2, 3, 4, 5], 1))
    # print(s.partitionArray([1, 2, 3, 4, 5], 6))