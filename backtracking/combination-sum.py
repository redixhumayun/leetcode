from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(current_sum, path, index):
            if current_sum == target:
                ans.append(path[:])
                return
            for i in range(index, len(candidates)):
                candidate = candidates[i]
                if current_sum + candidate <= target:        
                    current_sum += candidate
                    path.append(candidate)
                    backtrack(current_sum, path, i)
                    current_sum -= candidate
                    path.pop()
        ans = []
        backtrack(0, [], 0)
        return ans

    
if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    print(Solution().combinationSum(candidates, target))