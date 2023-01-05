
def find_all_arrangements(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_str
    """
    # Write your code here.
    #   Create sets for each of the possible attack vectors of a queen
    col_set = set()
    pos_dia_set = set()
    neg_dia_set = set()
    ans = []
    def backtrack(curr, num_of_queens, row_index):
        if num_of_queens == n:
            ans.append(curr[:])
            return
        if row_index >= n:
            return
        for col in range(0, n):
            pos_dia = row_index + col
            neg_dia = row_index - col
            if col not in col_set:
                if pos_dia not in pos_dia_set:
                    if neg_dia not in neg_dia_set:
                        col_set.add(col)
                        pos_dia_set.add(pos_dia)
                        neg_dia_set.add(neg_dia)
                        curr.append((row_index, col))
                        backtrack(curr, num_of_queens + 1, row_index + 1)
                        curr.pop()
                        neg_dia_set.remove(neg_dia)
                        pos_dia_set.remove(pos_dia)
                        col_set.remove(col)
    backtrack([], 0, 0)

    #   Generate output
    output = []
    for a in ans:
        ind = []
        for row, col in a:
            s = "-" * n
            s = s[:col] + "q" + s[col+1:]
            ind.append(s)
        output.append(ind)
    return output

if __name__ == "__main__":
    n = 4
    result = find_all_arrangements(n)
    print(result)

    n = 2
    result = find_all_arrangements(n)
    print(result)