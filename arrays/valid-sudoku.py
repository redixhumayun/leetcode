from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #   Brute force approach
        #   Iterate over 2D matrix along the diagonal and check each row and column first
        m = len(board)
        n = len(board[0])
        row = col = 0

        def check_list(array: list):
            hash_map = defaultdict(int)
            for num in array:
                try:
                    num = int(num)
                except ValueError:
                    continue
                hash_map[num] += 1
                if hash_map[num] > 1:
                    return False
            return True

        def check_row_and_cols():
            row = col = 0
            while row < m and col < n:
                #   Get the elements of the current row and current col
                current_row = board[row]
                current_col = [x[col] for x in board]
                row_result = check_list(current_row)
                col_result = check_list(current_col)
                if row_result == False or col_result == False:
                    return False
                row += 1
                col += 1
            return True

        def check_boxes():
            centers = ((1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7))
            for (row, col) in centers:
                hash_map = defaultdict(int)
                for i in range(row - 1, row + 2):
                    for j in range(col - 1, col + 2):
                        num = board[i][j]
                        try:
                            num = int(num)
                        except ValueError:
                            continue
                        hash_map[num] += 1
                        if hash_map[num] > 1:
                            return False
            return True

        
        result_1 = check_row_and_cols()
        result_2 = check_boxes()
        return result_1 and result_2

if __name__ == '__main__':
    print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
    print(Solution().isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))