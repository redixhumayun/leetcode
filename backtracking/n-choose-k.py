
def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    #   Create the array
    arr = [num for num in range(1, n+1)]

    def backtrack(i, curr):
        if len(curr) == k:
            ans.append(curr[:])
            return
        
        for j in range(i, len(arr)):
            curr.append(arr[j])
            backtrack(j + 1, curr)
            curr.pop()
    
    ans = []
    backtrack(0, [])
    return ans


if __name__ == '__main__':
    n = 5
    k = 2
    print(find_combinations(n, k))

    n = 6
    k = 6
    print(find_combinations(n, k))