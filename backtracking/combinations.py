from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(curr, index):
            if index > n+1:
                return
            if len(curr) == k:
                ans.append(curr[:])
                return
            for j in range(index, n+1):
                curr.append(j)
                backtrack(curr, j+1)
                curr.pop()

        backtrack([], 1)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))
    print(s.combine(1, 1))