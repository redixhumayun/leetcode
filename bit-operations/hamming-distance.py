class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        number = x ^ y
        count = 0
        mask = 1
        while mask <= number:
            result = number & mask
            if result > 0:
                count += 1
            mask = mask << 1
        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingDistance(1, 4))
    print( solution.hammingDistance(3, 1))