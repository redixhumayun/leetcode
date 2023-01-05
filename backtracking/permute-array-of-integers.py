
def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    ans = []
    t = len(arr)
    def backtrack(curr, num_arr):
        if len(curr) == t:
            ans.append(curr[:])
            return
        for index, num in enumerate(num_arr):
            curr.append(num)
            backtrack(curr, num_arr[:index] + num_arr[index+1:])
            curr.pop()
        return
    backtrack([], arr)
    return ans


if __name__ == "__main__":
    arr = [1, 2, 3]
    result = get_permutations(arr)
    print(result)

    arr = [1, 1, 2]
    result = get_permutations(arr)
    print(result)

    arr = [1, 2, 3, 4]
    result = get_permutations(arr)
    print(result)

    arr = [1, 2, 3, 4, 5]
    result = get_permutations(arr)
    print(result)