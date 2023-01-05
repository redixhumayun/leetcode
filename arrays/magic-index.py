def magic_index(arr):
    def binary_search(left, right):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == mid:
                return mid
            if arr[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    return binary_search(0, len(arr) - 1)

    #   O(n) solution
    # for index, num in enumerate(arr):
    #     if index == num:
    #         return index
    # return -1

if __name__ == '__main__':
    arr = [-1, 0, 1, 2, 4, 10]
    print(magic_index(arr))

    arr = [-4, -1, 0, 1, 2, 5, 7]
    print(magic_index(arr))