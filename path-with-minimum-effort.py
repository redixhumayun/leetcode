from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        seen = set()

        #   Recursive dfs
        def check_recursive(row, col, max_diff):
            def valid(row, col):
                return 0 <= row < m and 0 <= col < n

            if row == m - 1 and col == n - 1:
                return True
            directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    if abs(heights[new_row][new_col] - heights[row][col]) <= max_diff:
                        if check_recursive(new_row, new_col, max_diff):
                            return True
            return False

        #   Iterative dfs
        # def check(max_diff):
        #     def valid(row, col):
        #         return 0 <= row < m and 0 <= col < n

        #     directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
        #     stack = [(0, 0)]
        #     seen = {(0, 0)}
        #     while stack:
        #         (row, col) = stack.pop()
        #         if row == m - 1 and col == n - 1:
        #             return True
        #         for dx, dy in directions:
        #             new_row, new_col = row + dx, col + dy
        #             if valid(new_row, new_col) and (new_row, new_col) not in seen:
        #                 if abs(heights[new_row][new_col] - heights[row][col]) <= max_diff:
        #                     stack.append((new_row, new_col))
        #                 seen.add((new_row, new_col))
        #     return False

        left = 0
        right = float("-inf")
        for row in heights:
            for col in row:
                right = max(right, col)
        

        while left <= right:
            seen.clear()
            seen.add((0, 0))
            mid = (left + right) // 2
            if check_recursive(0, 0, max_diff=mid):
                right = mid - 1
            # if check(mid):
            #     right = mid - 1
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    s = Solution()
    print(s.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
    print(s.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
    print(s.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))