
def find_integer(arr):
    """
    Args:
     arr(list_int64)
    Returns:
     int64
    """
    # Write your code here.
    result = 0
    for num in arr:
        mask = 1 << num
        result = result | mask
    bin_string = "{0:b}".format(result)
    print(bin_string)
    # for index in range(len(bin_string) - 1, -1, -1):
    #     print(bin_string[index])
    # print(bin(result), result)
    # if len(bin(result)) < 2**32:
    #     return result + 1
    # return 0

if __name__ == '__main__':
    arr = [0, 1, 2, 3]
    print(find_integer(arr))

    arr = [1, 2, 3, 4, 5]
    print(find_integer(arr))

    arr = [4294967295, 399999999, 0]
    print(find_integer(arr))
    # arr = [5, 4, 3, 2, 1]
    # print(find_integer(arr))

    # arr = [5, 7, 6, 3, 1, 2, 4]
    # print(find_integer(arr))

    # arr = [1000000000]
    # print(find_integer(arr))

    # arr = [-400000, 0, 400000]
    # print(find_integer(arr))

    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(find_integer(arr))
