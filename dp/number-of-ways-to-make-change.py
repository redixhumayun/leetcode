
def number_of_ways(coins, amount):
    """
    Args:
     coins(list_int32)
     amount(int32)
    Returns:
     int32
    """
    # Write your code here.
    #   Bottom up code
    dp = [[0 for _ in range(amount + 1)] for _  in range(len(coins) + 1)]

    #   Fill up first column with 1's because the amount is zero and that is the base case
    for i in range(len(dp)):
        dp[i][0] = 1

    #   Start from last row and go left to right to fill up the table
    for i in range(len(coins) - 1, -1, -1):
        for j in range(1, amount+1):
            if coins[i] <= j:
                dp[i][j] = dp[i][j - coins[i]] + dp[i+1][j]
            else:
                dp[i][j] = dp[i+1][j]

    return dp[0][amount]

    # memo = {}
    # def helper(index, amount):
    #     if index >= len(coins):
    #         return 0
    #     if amount < 0:
    #         return 0
    #     if amount == 0:
    #         return 1

    #     if (index, amount) in memo:
    #         return memo[(index, amount)]

    #     memo[(index, amount)] = 0
    #     memo[(index, amount)] += helper(index, amount - coins[index]) + helper(index + 1, amount)
    #     return memo[(index, amount)]
    # return helper(0, amount)

if __name__ == "__main__":
    coins = [1, 2, 3]
    amount = 3
    print(number_of_ways(coins, amount))

    coins = [9, 1, 8, 10, 3]
    amount = 12
    print(number_of_ways(coins, amount))

    coins = [2, 7, 8, 12, 15, 5, 10, 3]
    amount = 99
    print(number_of_ways(coins, amount))