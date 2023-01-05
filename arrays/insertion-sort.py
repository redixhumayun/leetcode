
def insertion_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    for i in range(len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr


if __name__ == "__main__":
    arr = [8, 4, 2, 9, 3, 6]
    print(insertion_sort(arr))