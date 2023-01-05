class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_even = float("-inf")
        min_odd = float("inf")
        for num in A:
            if num > max_even and num % 2 == 0:
                max_even = num
            if num < min_odd and num % 2 == 1:
                min_odd = num
        return max_even - min_odd

if __name__ == "__main__":
    s = Solution()
    A = [0, 2, 9]
    print(s.solve(A))

    A = [5, 17, 100, 1]
    print(s.solve(A))

    A = [1, 2]
    print(s.solve(A))