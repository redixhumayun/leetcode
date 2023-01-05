from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result_flag = False
        for i in range(len(matrix)):
            leftPointer = 0
            rightPointer = len(matrix[i]) - 1
            if matrix[i][leftPointer] > target or matrix[i][rightPointer] < target:
                result_flag = False
                continue
            while leftPointer <= rightPointer:
                mid = (leftPointer + rightPointer) // 2
                num = matrix[i][mid]
                if num == target:
                    result_flag = True
                    return result_flag
                if num > target:
                    rightPointer = mid - 1
                else:
                    leftPointer = mid + 1
        return result_flag

if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
    print(s.searchMatrix([[1, 3]], 2))
    print(s.searchMatrix([[1, 3]], 3))
    print(s.searchMatrix([[1],[3]], 3))