class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        if x < 0:
            return False
        reversed = 0
        while x > 0:
            reversed = reversed * 10 + x % 10
            x = x // 10
        
        if reversed == temp:
            return True
        return False
        
if __name__ == '__main__':
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(-121))
    print(Solution().isPalindrome(10))
    print(Solution().isPalindrome(-101))
    print(Solution().isPalindrome(0))