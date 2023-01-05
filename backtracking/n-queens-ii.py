class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def backtrack(row, pos_diag_set, neg_diag_set, col_set):
            if row == n:
                return 1
            solutions = 0
            for col in range(n):
                if col in col_set:
                    continue
                pos_diag = row + col
                neg_diag = row - col
                if pos_diag not in pos_diag_set and neg_diag not in neg_diag_set:
                    col_set.add(col)
                    pos_diag_set.add(pos_diag)
                    neg_diag_set.add(neg_diag)
                    solutions += backtrack(row + 1, pos_diag_set, neg_diag_set, col_set)
                    col_set.remove(col)
                    pos_diag_set.remove(pos_diag)
                    neg_diag_set.remove(neg_diag)
            return solutions
        return backtrack(0, set(), set(), set())

if __name__ == "__main__":
    n = 4
    print(Solution().totalNQueens(n))