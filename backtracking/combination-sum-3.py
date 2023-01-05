from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(index, curr):
            if len(curr) == k and sum(curr) == n:
                ans.append(curr[:])
                return
            if len(curr) == k or sum(curr) > n:
                return
            
            for digit in range(index, 10):
                curr.append(digit)
                backtrack(digit + 1, curr)
                curr.pop()
        backtrack(1, [])
        return ans


        # #   Sanity check
        # sanity = 0
        # for i in range(k + 1):
        #     sanity += i
        # if sanity > n:
        #     return []

        # results = []
        # def backtrack(index, arr):
        #     if len(arr) == k:
        #         if sum(arr) == n:
        #             results.append(arr[:])
        #         return
        #     for d in range(index, 10):
        #         last_elem = None
        #         if len(arr) > 0:
        #             last_elem = arr[-1]
        #         if sum(arr) + d <= n and len(arr) < k and d != last_elem:
        #             arr.append(d)
        #             backtrack(d + 1, arr)
        #             arr.pop()
        # backtrack(1, [])
        # return results

if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum3(3, 7))
    print(solution.combinationSum3(3, 9))
    print(solution.combinationSum3(4, 1))
    print(solution.combinationSum3(1, 1))