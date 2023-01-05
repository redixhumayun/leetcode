class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        for i in range(0, len(A)):
            for j in range(i+1, len(A)):
                if A[i] + A[j] == B:
                    count += 1
        return count

if __name__ == "__main__":
    s = Solution()
    A = [1, 2, 3, 2, 1]
    B = 5
    print(s.solve(A, B))