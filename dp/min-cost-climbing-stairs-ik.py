
def min_cost_climbing_stairs(cost):
    """
    Args:
     cost(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    #   Bottom up tabulation
    n = len(cost)
    dp = [0] * (n+1)
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n+1):
        if i == n:
            dp[i] = min(dp[i-1], dp[i-2])
        else:
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    return dp[-1]

    #   Top down memoization
    # memo = {}
    # n = len(cost)
    # def dp(stair_index):
    #     if stair_index < 0:
    #         return float("inf")
    #     if stair_index == 0 or stair_index == 1:
    #         return 0
    #     if stair_index in memo:
    #         return memo[stair_index]
    #     memo[stair_index] = min(dp(stair_index - 1) + cost[stair_index - 1], dp(stair_index - 2) + cost[stair_index - 2])
    #     return memo[stair_index]
    # return dp(n)


if __name__ == "__main__":
    cost = [1, 1, 2]
    print(min_cost_climbing_stairs(cost))

    cost = [10, 15, 20]
    print(min_cost_climbing_stairs(cost))

    cost = [3, 4]
    print(min_cost_climbing_stairs(cost))

    cost = [100, 1]
    print(min_cost_climbing_stairs(cost))

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(min_cost_climbing_stairs(cost))