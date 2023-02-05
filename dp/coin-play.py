
def max_win(v):
    """
    Args:
     v(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    memo = {}
    def recurse(left, right):
        if left > right:
            return 0
        if right - left + 1 == 2:
            return max(v[left], v[right])

        if (left, right) in memo:
            return memo[(left, right)]
        #   At each recursive level, make a decision to take left or right
        #   If I take left, take an opponent decision that will minimise my value
        take_left = v[left] + min(recurse(left + 2, right), recurse(left + 1, right - 1))
        take_right = v[right] + min(recurse(left + 1, right - 1), recurse(left, right - 2))
        memo[(left, right)] = max(take_left, take_right)
        return memo[(left, right)]
    return recurse(0, len(v) - 1)


if __name__ == "__main__":
    coins = [8, 15, 3, 7]
    print(max_win(coins))

    coins = [8, 15, 3, 7, 6, 9, 16, 2]
    print(max_win(coins))

    coins = [1, 7, 3, 4, 5, 6]
    print(max_win(coins))

    coins = [149, 154, 63, 242, 12, 72, 65]
    print(max_win(coins))