class Solution:
    def findPlacement(self, x):
        counter = 0
        while x > 0:
            x = x // 10
            counter += 1
        return counter - 1

    def reverse(self, x: int) -> int:
        #   Handle negative numbers
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        counter = self.findPlacement(x)
        result = 0
        while counter >= 0:
            digit = x % 10
            result = result + digit * (10**counter)
            counter -= 1
            x = x // 10
        result = result * sign
        if result > 2**31-1 or result < -2**31:
            return 0
        return result


if __name__ == '__main__':
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))
    print(Solution().reverse(0))
    print(Solution().reverse(1534236469))
    print(Solution().reverse(-2147483648))