
def get_distinct_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    ans = []
    s = "".join(sorted(s))
    def backtrack(curr, index):
        if index == len(s):
            ans.append("".join(curr[:]))
            return

        curr.append(s[index])
        backtrack(curr, index + 1)
        curr.pop()

        while index + 1 < len(s) and s[index] == s[index + 1]:
            index += 1
        backtrack(curr, index + 1)
    
    backtrack([], 0)
    return ans

if __name__ == '__main__':
    print(get_distinct_subsets("abbc"))
