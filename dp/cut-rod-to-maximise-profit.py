
def get_maximum_profit(price):
    """
    Args:
     price(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    rod_length = len(price)
    memo = {}
    def dp(n):
        if n == 0:
            return 0
        if n == 1:
            return price[0]
        if n in memo:
            return memo[n]
        memo[n] = 0
        for i in range(1, n+1):
            memo[n] = max(memo[n], dp(n-i) + price[i-1])
        return memo[n]
    return dp(rod_length)


if __name__ == '__main__':
    price = [1, 5, 8, 9]
    print(get_maximum_profit(price))

    price = [1, 5, 8, 9, 10, 17, 17, 20]
    # print(get_maximum_profit(price))