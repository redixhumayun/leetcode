def merge_sort(arr):
    if len(arr) == 1:
        return arr
        
    division_point = len(arr) // 2
    
    left_arr = arr[:division_point]
    right_arr = arr[division_point:]

    #   Call the function recursively for the two halves
    left_arr_sorted = merge_sort(left_arr)
    right_arr_sorted = merge_sort(right_arr)

    #   Iterate over the arrays and merge them
    left_pointer = 0
    right_pointer = 0
    aux_array = []
    while left_pointer < len(left_arr_sorted) and right_pointer < len(right_arr_sorted):
        if left_arr_sorted[left_pointer] <= right_arr_sorted[right_pointer]:
            aux_array.append(left_arr_sorted[left_pointer])
            left_pointer += 1
        else:
            aux_array.append(right_arr_sorted[right_pointer])
            right_pointer += 1
    
    while left_pointer < len(left_arr_sorted):
        aux_array.append(left_arr_sorted[left_pointer])
        left_pointer += 1
    
    while right_pointer < len(right_arr_sorted):
        aux_array.append(right_arr_sorted[right_pointer])
        right_pointer += 1

    return aux_array

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(merge_sort(arr))

    arr = [5, 4, 3, 2, 1]
    print(merge_sort(arr))

    arr = [5, 8, 3, 9, 4, 1, 7]
    print(merge_sort(arr))