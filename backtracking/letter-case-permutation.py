
def letter_case_permutations(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    ans = set()
    def backtracking(curr, index):
        if index > len(s):
            return
        ans.add(curr[:])
        for i in range(index, len(s)):
            backtracking(curr[:i] + curr[i].upper() + curr[i+1:], i + 1)
            backtracking(curr[:i] + curr[i].lower() + curr[i+1:], i + 1)
    backtracking(s, 0)
    return list(ans)


if __name__ == "__main__":
    s = "a1z"
    result = letter_case_permutations(s)
    print(result)

    s = "G"
    result = letter_case_permutations(s)
    print(result)

    # s = "3z4"
    # result = letter_case_permutations(s)
    # print(result)