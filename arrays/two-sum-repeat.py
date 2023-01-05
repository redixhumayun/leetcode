from collections import defaultdict

def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    hash_map = defaultdict(int)
    for index in range(len(numbers)):
        x = target - numbers[index]
        if x in hash_map:
            return [hash_map[x], index]
        hash_map[numbers[index]] = index
    return [-1, -1]

if __name__ == '__main__':
    # print(pair_sum_sorted_array([1, 2, 3, 5, 10], 7))
    # print(pair_sum_sorted_array([-10, -7, -5, 0, 8, 10], 3))
    # print(pair_sum_sorted_array([-10, -7, -5, 0, 8, 10], -3))
    print(pair_sum_sorted_array([5, 3, 10, 45, 1], 6))