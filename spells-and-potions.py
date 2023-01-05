from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = [0] * len(spells)

        def findPotionIndex(target):
            firstPointer = 0
            lastPointer = len(potions) - 1
            while firstPointer <= lastPointer:
                midPointer = (firstPointer + lastPointer) // 2
                num = potions[midPointer]
                if target < num:
                    lastPointer = midPointer - 1
                else:
                    firstPointer = midPointer + 1
            return firstPointer

        for index, spell in enumerate(spells):
            min_required_potion = success / spell
            #   Find closest value to min_required_potion in potions
            insertion_index = findPotionIndex(min_required_potion)
            result[index] = len(potions) - insertion_index
        return result

if __name__ == "__main__":
    s = Solution()
    # print(s.successfulPairs([5,1,3], [1, 2, 3, 4, 5], 7))
    print(s.successfulPairs([3,1,2], [8, 5, 8], 16))
    # print(s.successfulPairs([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 7))
    # print(s.successfulPairs([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 8))
    # print(s.successfulPairs([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 9))
    # print(s.successfulPairs([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 10))
    # print(s.successfulPairs([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 11))
    # print(s.successfulPairs([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 12))
    # print(s.successfulPairs([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 13))
    # print(s.successfulPairs([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 14))
    # print(s.successfulPairs([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 15))
    # print(s.successfulPairs([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 16))