import math

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        #   First calculate the power
        ans = 1
        while B > 0:
            ans = (ans * A) % C
            B -= 1
        return ans
        # prod = 1
        # for i in range(1, B + 1):
        #     prod = prod * A
        # print(prod)
        # return prod % C

if __name__ == "__main__":
    A = 2
    B = 3
    C = 3
    D = Solution()
    print(D.pow(A, B, C))

    A = -5
    B = 3
    C = 3
    D = Solution()
    print(D.pow(A, B, C))

    A = 0
    B = 0
    C = 1
    D = Solution()
    print(D.pow(A, B, C))

    A = 213
    B = 231
    C = 1
    D = Solution()
    print(D.pow(A, B, C))

    A = 2
    B = 0
    C = 1
    D = Solution()
    print(D.pow(A, B, C))

    A = -1
    B = 1
    C = 20
    D = Solution()
    print(D.pow(A, B, C))

    A = 71045970
    B = 41535484
    C = 64735492
    D = Solution()
    print(D.pow(A, B, C))