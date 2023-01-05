
def find_intersection(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    def find_min_and_increment(pointer_1, pointer_2, pointer_3):
        #   Find the min value among all three arrays and increment that one
        value1 = arr1[pointer_1]
        value2 = arr2[pointer_2]
        value3 = arr3[pointer_3]
        min_value = min(value1, min(value2, value3))
        if value1 == min_value:
            return pointer_1 + 1, pointer_2, pointer_3
        if value2 == min_value:
            return pointer_1, pointer_2 + 1, pointer_3
        if value3 == min_value:
            return pointer_1, pointer_2, pointer_3 + 1
        else:
            raise Exception("Something went wrong")

    output = []
    pointer_1 = pointer_2 = pointer_3 = 0
    while pointer_1 < len(arr1) and pointer_2 < len(arr2) and pointer_3 < len(arr3):
        if arr1[pointer_1] == arr2[pointer_2] == arr3[pointer_3]:
            output.append(arr1[pointer_1])
            pointer_1 += 1
            pointer_2 += 1
            pointer_3 += 1
            continue
        pointer_1, pointer_2, pointer_3 = find_min_and_increment(pointer_1, pointer_2, pointer_3)
    
    if len(output) == 0:
        return [-1]
    return output


if __name__ == '__main__':
    arr1 = [2, 5, 10]
    arr2 = [2, 3, 4, 10]
    arr3 = [2, 4, 10]
    print(find_intersection(arr1, arr2, arr3))

    arr1 = [1, 2, 3]
    arr2 = []
    arr3 = [2, 2]
    print(find_intersection(arr1, arr2, arr3))

    arr1 = [1, 2, 2, 2, 9]
    arr2 = [1, 1, 2, 2]
    arr3 = [1, 1, 1, 2, 2, 2]
    print(find_intersection(arr1, arr2, arr3))

    # arr1 = [6, 7, 8, 10, 11, 12]
    # arr2 = [8, 9, 10, 11, 12]
    # arr3 = [8, 10, 11, 12, 13, 14]
    # print(find_intersection(arr1, arr2, arr3))

    # arr1 = [1, 5, 10, 20, 40, 80]
    # arr2 = [6, 7, 20, 80, 100]
    # arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
    # print(find_intersection(arr1, arr2, arr3))

    # arr1 = [1, 5, 5]
    # arr2 = [3, 4, 5, 5, 10]
    # arr3 = [5, 5, 10, 20]
    # print(find_intersection(arr1, arr2, arr3))

    # arr1 = [1, 5, 5]
    # arr2 = [3, 4, 5, 5, 10]
    # arr3 = [5, 5, 10, 20]
    # print(find_intersection(arr1, arr2, arr3))

    # arr1 = [1, 5, 5]
    # arr2 = [3, 4, 5, 5, 10]
    # arr3 = [5, 5, 10, 20]
    # print(find_intersection(arr1, arr2, arr3))

    # arr1 = [1, 5, 5]
    # arr2 = [3, 4, 5, 5, 10]
    # arr3 = [5, 5, 10, 20]
    # print(find_intersection(arr1, arr2, arr3))

    # arr1 = [1, 5, 5]
    # arr2 = [3, 4, 5, 5, 10]
    # arr3 = [5, 5, 10, 20]
    # print(find_intersection(arr1, arr2, arr3))

    # arr1 = [1, 5, 5]
    # arr2 = [3, 4, 5, 5,