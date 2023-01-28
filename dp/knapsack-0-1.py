"""
This is the classic Knapsack with repetition allowed problem. It's the same as the coin change problem.
The idea here is to maximize the value of the items picked but keeping the overall weight of the items
below the weight value.

Time complexity -> O(n*W), where n is the number of items and W is the allowed weight limit
Space complexity -> O(n*W), same as above
"""
def knapsack_with_repetition(weights, values, weight) -> int:
    dp = [0] * (weight + 1)
    dp[0] = 0 # If the available weight is zero, no items can be picked up and thus no value
    for i in range(1, len(dp)):
        ans = 0
        for index, w in enumerate(weights):
            if w <= i:
               ans = max(ans, dp[i - w] + values[index])
        dp[i] = ans 
    print(dp)
    return dp[weight]

if __name__ == "__main__":
    weights = [6, 3, 4, 2]
    values = [30, 14, 16, 9]
    weight = 10
    print(knapsack_with_repetition(weights, values, weight))