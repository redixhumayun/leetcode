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
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
    arr[start], arr[smaller] = arr[smaller], arr[start]
    #   Call helper function for left half of arr
    helper(arr, start, smaller - 1)
    #   Call helper function for right half of arr
    helper(arr, smaller + 1, end)

    return arr
            

def quick_sort(arr):
    return helper(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(quick_sort(arr))

    arr = [5, 4, 3, 2, 1]
    print(quick_sort(arr))

    arr = [5, 7, 6, 3, 1, 2, 4]
    print(quick_sort(arr))

    arr = [1000000000]
    print(quick_sort(arr))