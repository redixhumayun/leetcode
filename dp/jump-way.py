
def jump_ways(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    #   Iterative approach
    dp = [0] * (n+1)
    dp[n] = 1
    dp[n-1] = 1
    for i in range(n-2, -1, -1):
        dp[i] = dp[i+1] + dp[i+2]
    return dp[0]

    #   Recursive code
    # memo = {}
    # def helper(number):
    #     if number > n:
    #         return 0
    #     if number == n:
    #         return 1
    #     if number in memo:
    #         return memo[number]
    #     ans = 0
    #     for i in [1, 2]:
    #         ans += helper(number + i)
    #     memo[number] = ans
    #     return memo[number]
    # return helper(0)


if __name__ == "__main__":
    n = 3
    print(jump_ways(n))