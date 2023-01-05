from typing import List

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def check(chunk_sweetness):
            total = count = 0
            for chunk in sweetness:
                total += chunk
                if total >= chunk_sweetness:
                    total = 0
                    count += 1
                    if count >= k+1:
                        return True
            if count < k+1:
                return False

        left = min(sweetness)
        right = sum(sweetness) / (k+1)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return int(right)

if __name__ == "__main__":
    sweetness = [1,2,2,1,2,2,1,2,2]
    k = 2
    print(Solution().maximizeSweetness(sweetness, k))