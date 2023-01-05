import math
from random import randrange

def helper(arr, start, end):
    if start >= end:
        return arr
    pivot_index = randrange(start, end + 1)
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    smaller = start
    for bigger in range(start, end + 1):
        if arr[bigger] < arr[start]:
            smaller += 1
            arr[bigger], arr[smaller] = arr[smaller], arr[bigger]

    arr[start], arr[smaller] = arr[smaller], arr[start]
    helper(arr, start, smaller - 1)
    helper(arr, smaller + 1, end)

    return arr

def sort_array(arr):
    """
    Args:
     arr(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    #   This approach uses counting sort
    min_elem = float("inf")
    max_elem = float("-inf")
    for char in arr:
        min_elem = min(min_elem, ord(char))
        max_elem = max(max_elem, ord(char))
    
    k = math.floor(max_elem - min_elem)
    counts = [0] * (k + 1)
    for char in arr:
        counts[ord(char) - int(min_elem)] += 1

    output = [None] * len(arr)
    output_index = 0
    for index, count in enumerate(counts):
        for _ in range(count):
            output[output_index] = chr(index + int(min_elem))
            output_index += 1
    return output

    #   This approach uses quicksort
    # return helper(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    arr = ["a", "s", "d", "f", "g", "*", "&", "!", "z", "y"]
    print(sort_array(arr))

    arr = ['b', 'a', 'c', 'd', 'e', 'f']
    print(sort_array(arr))

    arr = ['c']
    print(sort_array(arr))