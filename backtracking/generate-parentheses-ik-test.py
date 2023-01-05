
def find_all_well_formed_brackets(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    # Write your code here.
    ans = []
    def backtrack(curr, score):
        if score < 0:
            return
        if len(curr) > 2 * n:
            return
        if len(curr) == 2 * n and score == 0:
            ans.append("".join(curr[:]))
            return
        
        #   Add a left paren as the first choice
        curr.append("(")
        backtrack(curr, score + 1)
        curr.pop()

        #   Add a right paren as the second choice
        curr.append(")")
        backtrack(curr, score - 1)
        curr.pop()

    backtrack([], 0)
    return ans


if __name__ == '__main__':
    print(find_all_well_formed_brackets(2))
    print(find_all_well_formed_brackets(3))