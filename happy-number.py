class Solution:
    def sumOfSquareDigits(self, n):
        sum = 0
        while n > 0:
            digit = n % 10
            n = n // 10
            sum += digit ** 2
        return sum

    def isHappy(self, n: int) -> bool:
        hashset = set()
        while n not in hashset:
            hashset.add(n)
            n = self.sumOfSquareDigits(n)
        if n == 1 or n == 10:
            return True
        else:
            return False

if __name__ == "__main__":
    n = 19
    result = Solution().isHappy(n)
    print(result)

    n = 2
    result = Solution().isHappy(n)
    print(result)

    n = 75
    result = Solution().isHappy(n)
    print(result)