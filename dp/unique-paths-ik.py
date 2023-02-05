
def unique_paths(n, m):
    """
    Args:
     n(int32)
     m(int32)
    Returns:
     int32
    """
    # Write your code here.

    #   Bottom up implementation
    #   Adding an extra row & column of zeroes to pad the result so that negative indexes don't matter
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    dp[1][1] = 1
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            if i == 1 and j == 1:
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][m]

    #   Recursive approach with memoization

    # memo = {}
    
    # def helper(row, col):
    #     if row < 0 or col < 0:
    #     #   Out of bounds, no way to get here
    #         return 0
    #     if row == 0 and col == 0:
    #         #   Start point, one way to get here
    #         return 1
    #     if (row, col) in memo:
    #         return memo[(row, col)]
    #     memo[(row, col)] = helper(row - 1, col) + helper(row, col - 1)
    #     return memo[(row, col)]
    # return helper(n-1, m-1)

if __name__ == '__main__':
    n = 3
    m = 2
    print(unique_paths(n, m))

    n = 5
    m = 3
    print(unique_paths(n, m))

    n = 4
    m = 1
    print(unique_paths(n, m))