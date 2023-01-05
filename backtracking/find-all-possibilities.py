
def find_all_possibilities(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    def backtrack(curr, index):
        if index == len(s):
            ans.append("".join(curr[:]))
            return
        if s[index] == '?':
            curr.append('0')
            backtrack(curr, index + 1)
            curr.pop()
            curr.append('1')
            backtrack(curr, index + 1)
            curr.pop()
        else:
            curr.append(s[index])
            backtrack(curr, index + 1)
            curr.pop()
        return
    ans = []
    backtrack([], 0)
    return ans


if __name__ == '__main__':
    print(find_all_possibilities("1?10"))
    print(find_all_possibilities("1?0?"))
    print(find_all_possibilities("1001011010010011011111001111010010111011111"))