from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        hash_A = defaultdict(int)
        hash_B = defaultdict(int)
        
        #   Count occurrences of A
        for num in A:
            hash_A[num] += 1
        
        for num in B:
            hash_B[num] += 1

        print(hash_A, hash_B)

        output = []
        for key in hash_A.keys():
            if key in hash_B:
                for _ in range(min(hash_A[key], hash_B[key])):
                    output.append(key)

        return output

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = [5, 4, 3, 2, 1]
    C = Solution()
    print(C.solve(A, B))

    A = [1, 2, 2, 1]
    B = [2, 3, 1, 2]
    C = Solution()
    print(C.solve(A, B))

    A = [2, 1, 4, 10]
    B = [3, 6, 2, 10, 10]
    C = Solution()
    print(C.solve(A, B))