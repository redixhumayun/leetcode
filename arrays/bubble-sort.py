
def bubble_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j-1]:
                #   swap the two elems
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(bubble_sort(arr))

    arr = [5, 4, 3, 2, 1]
    print(bubble_sort(arr))

    arr = [5, 8, 3, 9, 4, 1, 7]
    print(bubble_sort(arr))