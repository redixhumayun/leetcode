from collections import defaultdict

def solve_sudoku_puzzle(board):
    """
    Args:
     board(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    m = len(board)

    def find_square(row, col):
        #   This helper method will determine which square needs to be currently looked at
        if 0 <= row <= 2:
            if 0 <= col <= 2:
                return 1
            elif 3 <= col <= 5:
                return 2
            else:
                return 3
        elif 3 <= row <= 5:
            if 0 <= col <= 2:
                return 4
            elif 3 <= col <= 5:
                return 5
            else:
                return 6
        else:
            if 0 <= col <= 2:
                return 7
            elif 3 <= col <= 5:
                return 8
            else:
                return 9

    row_hm = defaultdict(set)
    col_hm = defaultdict(set)
    square_hm = defaultdict(set)

    def preprocess_board():
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != 0:
                    row_hm[row].add(board[row][col])
                    col_hm[col].add(board[row][col])
                    square_hm[find_square(row, col)].add(board[row][col])

    def could_place(number, row, col):
        square = find_square(row, col)
        return number not in row_hm[row] \
            and number not in col_hm[col] \
            and number not in square_hm[square]

    ans = []
    def backtrack(row_index, col_index):
        nonlocal ans
        if row_index >= m:
            ans = [row[:] for row in board]
            return
        if board[row_index][col_index] == 0:
            for num in range(1, 10):
                if could_place(num, row_index, col_index):
                    square = find_square(row_index, col_index)
                    row_hm[row_index].add(num)
                    col_hm[col_index].add(num)
                    square_hm[square].add(num)
                    board[row_index][col_index] = num
                    if col_index == m - 1:
                        backtrack(row_index + 1, 0)
                    else:
                        backtrack(row_index, col_index + 1)
                    board[row_index][col_index] = 0
                    square_hm[square].remove(num)
                    col_hm[col_index].remove(num)
                    row_hm[row_index].remove(num)
        else:
            if col_index == m - 1:
                backtrack(row_index + 1, 0)
            else:
                backtrack(row_index, col_index + 1)
        
    preprocess_board()
    backtrack(0, 0)
    return ans


if __name__ == "__main__":
    board = [[8, 4, 9, 0, 0, 3, 5, 7, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0],
                [7, 0, 0, 0, 9, 0, 0, 8, 3],
                [0, 0, 0, 9, 4, 6, 7, 0, 0],
                [0, 8, 0, 0, 5, 0, 0, 4, 0],
                [0, 0, 6, 8, 7, 2, 0, 0, 0],
                [5, 7, 0, 0, 1, 0, 0, 0, 4],
                [0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 2, 1, 7, 0, 0, 8, 6, 5]
            ]
    print(solve_sudoku_puzzle(board))