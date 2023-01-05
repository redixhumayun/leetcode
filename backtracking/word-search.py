from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n
        def dfs(row, col, current_word, index) -> bool:
            result = False
            if current_word == word:
                result = True
                return True
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if isValid(new_row, new_col) and (new_row, new_col) not in seen and board[new_row][new_col] == word[index+1]:
                    seen.add((new_row, new_col))
                    result = result or dfs(new_row, new_col, current_word + board[new_row][new_col], index + 1)
                    seen.remove((new_row, new_col)) 
            return result
        #   Define valid directions of movement
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        #   Find all occurrences of the first letter
        occurrences = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    occurrences.add((i, j))
        
        seen = set()
        overall_result: bool = False
        for occurrence in occurrences:
            #   Perform DFS from this cell
            (row, col) = occurrence
            seen.add((row, col))
            overall_result = overall_result or dfs(row, col, board[row][col], 0)
            seen.remove((row, col))
        return overall_result

if __name__ == "__main__":
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word = "ABCCED"
    print(Solution().exist(board, word))
    
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    print(Solution().exist(board, word))

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    print(Solution().exist(board, word))

    board = [["S", "E", "E", "D"]]
    word = "SEED"
    print(Solution().exist(board, word)) 

    board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
    word = "AAAAAAAAAAAABAA"
    print(Solution().exist(board, word))