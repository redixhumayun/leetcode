
def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    ans = []
    def backtrack(curr, arr):
        if len(arr) == 0:
            ans.append(curr[:])
            return
        for index, num in enumerate(arr):
            curr.append(num)
            backtrack(curr, arr[:index] + arr[index+1:])
            curr.pop()
    backtrack([], arr)
    return ans


if __name__ == '__main__':
    print(get_permutations([1, 2, 3]))