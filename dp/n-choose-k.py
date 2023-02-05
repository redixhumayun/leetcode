
def ncr(n, r):
    """
    Args:
     n(int32)
     r(int32)
    Returns:
     int32
    """
    # Write your code here.
    #optimised bottom up implementation uses O(k) space
    first_row = [0] * (r+1)
    second_row = [0] * (r+1)
    for index, col in enumerate(second_row):
        if index <= 1:
            second_row[index] = 1

    for index in range(2, n+1):
        temp_row = [0] * (r+1)
        for index in range(len(temp_row)):
            if index != 0:
                temp_row[index] = second_row[index] + second_row[index-1]
            else:
                temp_row[index] = second_row[index]
        second_row = temp_row

    return second_row[-1]
    

    #   Bottom up implementation uses O(nk) space
    # dp = [[-1 for j in range(r+1)] for i in range(n+1)]
    # for row in range(len(dp)):
    #     for col in range(len(dp[row])):
    #         if row == col or col == 0:
    #             dp[row][col] = 1
    #         if row < col:
    #             dp[row][col] = 0
    #         if col == 1:
    #             dp[row][col] = row

    # for n in range(len(dp)):
    #     for k in range(len(dp[n])):
    #         if dp[n][k] == -1:
    #             dp[n][k] = dp[n-1][k] + dp[n-1][k-1]
    # return dp[n][r]

    #   Top down implementation
    # memo = {}
    # def helper(n, k):
    #     if k == 0 or k == n:
    #         return 1
    #     if k == 1:
    #         return n
    #     if n < k:
    #         return 0
    #     if (n, k) in memo:
    #         return memo[(n, k)]
    #     memo[(n, k)] = (helper(n-1, k) + helper(n-1, k-1)) % (10**9 + 7)
    #     return memo[(n, k)]
    # return helper(n, r)


if __name__ == '__main__':
    n = 5
    r = 3
    print(ncr(n, r))

    n = 6
    r = 0
    print(ncr(n, r))