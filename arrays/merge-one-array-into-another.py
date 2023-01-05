
def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    #   Use three pointers to compare elements at the end of the first and second arrays
    #   and decide which elements to put into the 0 slots
    pointer_1 = len(first) - 1
    pointer_2 = len(first) - 1
    pointer_3 = len(second) - 1
    while pointer_1 > -1 and pointer_2 > -1:
        if first[pointer_1] > second[pointer_2]:
            second[pointer_3] = first[pointer_1]
            pointer_1 -= 1
            pointer_3 -= 1
        else:
            second[pointer_3] = second[pointer_2]
            pointer_2 -= 1
            pointer_3 -= 1
    while pointer_1 >= 0:
        second[pointer_3] = first[pointer_1]
        pointer_3 -= 1
        pointer_1 -= 1
    while pointer_2 >= 0:
        second[pointer_3] = second[pointer_2]
        pointer_3 -= 1
        pointer_2 -= 1
    return second

    # Write your code here.
    #   Copy elements of first array into second array starting at the first zero
    #   Sort the result array
    #   O(n * log n)
    # first_arr_pointer = 0
    # second_arr_pointer = len(first)
    # while first_arr_pointer < len(first):
    #     second[second_arr_pointer] = first[first_arr_pointer]
    #     first_arr_pointer += 1
    #     second_arr_pointer += 1
    # second.sort()
    # return second


if __name__ == '__main__':
    print(merge_one_into_another([1, 3, 5], [2, 4, 6, 0, 0, 0]))