
def merge_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    if len(arr) == 1:
        return arr
    div_index = len(arr) // 2
    left_array = arr[:div_index]
    right_array = arr[div_index:]
    
    left_sorted = merge_sort(left_array)
    right_sorted = merge_sort(right_array)
    
    left_pointer = right_pointer = 0
    output_arr = []
    while left_pointer < len(left_sorted) and right_pointer < len(right_sorted):
        if left_sorted[left_pointer] <= right_sorted[right_pointer]:
            output_arr.append(left_sorted[left_pointer])
            left_pointer += 1
        else:
            output_arr.append(right_sorted[right_pointer])
            right_pointer += 1

    while left_pointer < len(left_sorted):
        output_arr.append(left_sorted[left_pointer])
        left_pointer += 1

    while right_pointer < len(right_sorted):
        output_arr.append(right_sorted[right_pointer])
        right_pointer += 1
        
    return output_arr

if __name__ == '__main__':
    print(merge_sort([5, 8, 3, 9, 4, 1, 7]))
    print(merge_sort([]))