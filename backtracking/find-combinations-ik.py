
def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    ans = []
    def backtrack(curr, index):
        if index > n:
            return
        if len(curr) == k:
            ans.append(curr[:])
            return
        for i in range(index, len(arr)):
            curr.append(arr[i])
            backtrack(curr, i + 1)
            curr.pop()

    #   Generate an array of numbers from 1 to n
    arr = [x for x in range(1, n+1)]
    backtrack([], 0)
    return ans

if __name__ == "__main__":
    n = 5
    k = 2
    result = find_combinations(n, k)
    print(result)

    n = 1
    k = 1
    result = find_combinations(n, k)
    print(result)

    n = 6
    k = 6
    result = find_combinations(n, k)
    print(result)

    # n = 9
    # k = 3
    # result = find_combinations(n, k)
    # print(result)

    # n = 20
    # k = 4
    # result = find_combinations(n, k)
    # print(result)