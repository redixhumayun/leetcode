
def calculate_power(a, b):
    """
    Args:
     a(int64)
     b(int64)
    Returns:
     int32
    """
    # Write your code here.
    if b == 0:
        return 1
    if b == 1:
        return a
    if b % 2 == 0:
        return ((calculate_power(a, b / 2)) ** 2) % 1000000007
    else:
        return (calculate_power(a, b - 1) * a) % 1000000007


if __name__ == '__main__':
    print(calculate_power(2, 10))
    print(calculate_power(10**4, 10**7))