
def selection_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    for i, num in enumerate(arr):
        min_value = arr[i]
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < min_value:
                min_value = arr[j]
                min_index = j
        
        #   Swap the two values
        temp = arr[i]
        arr[i] = min_value
        arr[min_index] = temp
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(selection_sort(arr))

    arr = [5, 4, 3, 2, 1]
    print(selection_sort(arr))

    arr = [5, 8, 3, 9, 4, 1, 7]
    print(selection_sort(arr))