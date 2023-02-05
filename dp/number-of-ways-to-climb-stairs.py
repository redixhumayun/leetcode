
def count_ways_to_climb(steps, n):
    """
    Args:
     steps(list_int32)
     n(int32)
    Returns:
     int64
    """
    # Write your code here
    memo = {}
    def helper(number_of_steps):
        if number_of_steps < 0:
            return 0
        if number_of_steps == 0:
            return 1
        if number_of_steps in memo:
            return memo[number_of_steps]
        ans = 0
        for step in steps:
            ans += helper(number_of_steps - step)
        memo[number_of_steps] = ans
        return memo[number_of_steps]
    return helper(n)

if __name__ == "__main__":
    steps = [1, 2]
    n = 3
    print(count_ways_to_climb(steps, n))

    steps = [1, 3, 5]
    n = 5
    print(count_ways_to_climb(steps, n))

    steps = [2, 3]
    n = 7
    print(count_ways_to_climb(steps, n))