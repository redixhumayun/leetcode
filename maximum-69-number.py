class Solution:
    def findDivisor(self, num):
        start = 1
        while (num // (10**start)) > 0:
            start += 1
        return 10**(start-1)

    def maximum69Number (self, num: int) -> int:
        divisor = self.findDivisor(num)
        ans = 0
        count = 0
        while divisor != 1:
            digit = num // divisor
            if digit == 6 and count == 0:
                ans += 9 * divisor
                count += 1
            else:
                ans += digit * divisor
            remainder = num % divisor
            num = remainder
            divisor = divisor // 10
        if num == 6 and count == 0:
            ans += 9 * divisor
        else:
            ans += num * divisor
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maximum69Number(9669))
    print(s.maximum69Number(9996))
    print(s.maximum69Number(9999))