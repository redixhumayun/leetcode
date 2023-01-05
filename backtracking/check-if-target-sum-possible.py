
def check_if_sum_possible(arr, k):
    """
    Args:
     arr(list_int64)
     k(int64)
    Returns:
     bool
    """
    # Write your code here.
    ans = []
    def backtrack(curr, index):
        if len(curr) > 0 and sum(curr) == k:
            ans.append(curr[:])
            return
        if index == len(arr):
            return
        
        curr.append(arr[index])
        backtrack(curr, index + 1)
        curr.pop()

        backtrack(curr, index + 1)
    
    backtrack([], 0)
    if len(ans) == 0:
        return False
    return True


if __name__ == "__main__":
    arr = [2, 4, 8]
    k = 6
    result = check_if_sum_possible(arr, k)
    print(result)

    arr = [2, 4, 6]
    k = 5
    result = check_if_sum_possible(arr, k)
    print(result)

    arr = [1]
    k = 0
    result = check_if_sum_possible(arr, k)
    print(result)