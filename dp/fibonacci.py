
def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    # Write your code here.
    #   Iterative code
    arr = [0] * (n+1)
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

    #   Recursive code
    # memo = {}
    # def helper(n):
    #     if n == 0 or n == 1:
    #         return n
    #     if n in memo:
    #         return memo[n]
    #     memo[n] = helper(n-1) + helper(n-2)
    #     return memo[n]
    # return helper(n)

if __name__ == "__main__":
    n = 10
    print(find_fibonacci(n))