from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        weight = 0
        firstPointer = 0
        lastPointer = len(people) - 1
        while lastPointer >= firstPointer:
            if people[firstPointer] + people[lastPointer] <= limit:
                firstPointer += 1
            
            lastPointer -= 1
            count += 1
        return count

if __name__ == '__main__':
    s = Solution()
    # print(s.numRescueBoats([1,2], 3))
    # print(s.numRescueBoats([3,2,2,1], 3))
    # print(s.numRescueBoats([3,5,3,4], 5))
    print(s.numRescueBoats([2,4], 5))