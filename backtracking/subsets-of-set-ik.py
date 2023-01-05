
def generate_all_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    ans = []
    def backtrack(curr, index):
        ans.append("".join(curr[:]))
        for i in range(index, len(s)):
            curr.append(s[i])
            backtrack(curr, i + 1)
            curr.pop()

    backtrack([], 0)
    return ans


if __name__ == '__main__':
    print(generate_all_subsets("abcde"))