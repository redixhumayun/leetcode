
def counting_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    #   Find the max element in the array
    max_elem = float("-inf")
    min_elem = float("inf")
    for num in arr:
        max_elem = max(max_elem, num)
        min_elem = min(min_elem, num)

    k = max_elem - min_elem
    
    #   Initialize array of size max_elem + 1
    counts = [0] * (k + 1)  # type: ignore
    for num in arr:
        counts[num - min_elem] += 1

    output = [None] * len(arr)
    output_index = 0
    for index, count in enumerate(counts):
        for _ in range(count):
            output[output_index] = index + min_elem
            output_index += 1
    return output


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(counting_sort(arr))

    arr = [5, 4, 3, 2, 1]
    print(counting_sort(arr))

    arr = [5, 7, 6, 3, 1, 2, 4]
    print(counting_sort(arr))

    # arr = [1000000000]
    # print(counting_sort(arr))

    arr = [-400000, 0, 400000]
    print(counting_sort(arr))

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(counting_sort(arr))

    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(counting_sort(arr))

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(counting_sort(arr))

    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(counting_sort(arr))

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(counting_sort(arr))