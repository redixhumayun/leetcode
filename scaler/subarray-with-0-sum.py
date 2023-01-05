class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        #   Create a set to count the prefix sum so far
        #   Add zero to it to account for sub-arrays that start from 0
        set = {0}

        total = 0
        for num in A:
            total += num
            if total in set:
                return 1
            set.add(total)
        return 0

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = Solution()
    print(B.solve(A))

    #   Create a list of positive and negative integers
    A = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2, -2]
    B = Solution()
    print(B.solve(A))

    A = [-1, 1]
    B = Solution()
    print(B.solve(A))

    A = [-4, -3, 0, 2, 1]
    B = Solution()
    print(B.solve(A))
    