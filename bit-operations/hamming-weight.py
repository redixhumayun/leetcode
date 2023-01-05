class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        mask = 1
        while mask <= n:
            result = n & mask
            if result > 0:
                count += 1
            mask = mask << 1
        return count
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingWeight(11))
    print(solution.hammingWeight(128))