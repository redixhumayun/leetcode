from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        start = end = 0
        output = []
        visited = set()
        while start <= m // 2 and end <= n // 2:
            for col in range(start, n - end, 1):
                if (start, col) not in visited:
                    output.append(matrix[start][col])
                    visited.add((start, col))
            for row in range(start + 1, m - end - 1, 1):
                if (row, n - end - 1) not in visited:
                    output.append(matrix[row][n - end - 1])
                    visited.add((row, n - end - 1))
            for col in range(n - end - 1, start, -1):
                if (m - end - 1, col) not in visited:
                    output.append(matrix[m - end - 1][col])
                    visited.add((m - end - 1, col))
            for row in range(m - end - 1, start, -1):
                if (row, start) not in visited:
                    output.append(matrix[row][start])
                    visited.add((row, start))
            start += 1
            end += 1
        return output

if __name__ == "__main__":
    matrix = [
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]
            ]
    result = Solution().spiralOrder(matrix)
    print(result)

    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]
    result = Solution().spiralOrder(matrix)
    print(result)

    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    result = Solution().spiralOrder(matrix)
    print(result)

    matrix = [
        [7],
        [9],
        [6]
    ]
    result = Solution().spiralOrder(matrix)
    print(result)