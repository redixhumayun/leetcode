from typing import List

class Solution:
    def convertToNumber(self, array) -> int:
        num = 0
        for i in range(len(array)):
            num += array[i] * 10 ** (len(array) - i - 1)
        return num

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        results = set()
        def backtrack(arr, difference):
            if len(arr) == n:
                results.add(self.convertToNumber(arr[:]))
                return
            for diff in [k, -k]:
                if 0 <= arr[-1] + diff < 10:
                    arr.append(arr[-1] + diff)
                    backtrack(arr, -difference)
                    arr.pop()
                

        for i in range(1, 10, 1):
            backtrack([i], k)
            
        return list(results)
    
if __name__ == "__main__":
    n = 3
    k = 7
    print(Solution().numsSameConsecDiff(n, k))

    n = 2
    k = 0
    r = Solution().numsSameConsecDiff(n, k)
    print(sorted(r))

    n = 3
    k = 1
    r = Solution().numsSameConsecDiff(n, k)
    print(sorted(r))