class Solution:
    def mySqrt(self, x: int) -> int:
        def check(num):
            if num**2 > x:
                return False
            return True
        
        left = 0
        right = x + 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                 left = mid + 1
            else:
                right = mid - 1
        return left - 1

if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(4))
    # print(s.mySqrt(8))
    # print(s.mySqrt(1))
    # print(s.mySqrt(0))
    # print(s.mySqrt(2147395599))