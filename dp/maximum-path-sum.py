
def maximum_path_sum(grid):
    """
    Args:
     grid(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    m = len(grid)
    n = len(grid[0])

    #   Bottom up approach - tabulation with reduced memory
    dp = [0] * (m+1)
    for i in range(1, m+1):
        temp = [0] * (n+1)
        for j in range(1, len(temp)):
            temp[j] = max(temp[j-1], dp[j]) + grid[i-1][j-1]
        dp = temp
    return dp[-1]

    #   Bottom up approach - tabulation
    # dp = [[0 for i in range(n+1)] for j in range(m+1)]
    # dp[1][1] = grid[0][0]
    # for i in range(1, m+1):
    #     for j in range(1, n+1):
    #         dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
    # return dp[m][n]

    #   Top down approach
    
    # memo = {}
    # def dp(row, col):
    #     if row == 0 and col == 0:
    #         return grid[row][col]
    #     if row < 0 or col < 0:
    #         return float("-inf")
    #     if (row, col) in memo:
    #         return memo[(row, col)]
    #     memo[(row, col)] = max(dp(row-1, col), dp(row, col-1)) + grid[row][col]
    #     return memo[(row, col)]
    # return dp(m-1, n-1)


if __name__ == "__main__":
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    # print(maximum_path_sum(grid))

    grid = [
        [4, 5, 8],
        [3, 6, 4],
        [2, 4, 7]
    ]
    print(maximum_path_sum(grid))

    grid = [
        [1, -4, 3],
        [4, -2, 2]
    ]
    # print(maximum_path_sum(grid))

    grid = [[1]]
    # print(maximum_path_sum(grid))