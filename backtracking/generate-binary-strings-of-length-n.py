
def get_binary_strings(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    # Write your code here.
    ans = []
    def backtrack(curr):
        if len(curr) == n:
            ans.append(curr[:])
            return
        for choice in [0, 1]:
            curr.append(choice)
            backtrack(curr)
            curr.pop()
    backtrack([])

    #   Write a lambda function mapping over the elements of ans
    #   and converting them to strings
    ans = list(map(lambda x: "".join(map(str, x)), ans))
    return ans


if __name__ == '__main__':
    print(get_binary_strings(3))