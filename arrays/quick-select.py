from random import randrange

def quickselect(nums, left, right, index) -> int:  # type: ignore
    pivot_index = randrange(left, right + 1)
    pivot_element = nums[pivot_index]
    pointer = left

    #   Swap the pivot element with the right element
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    for i in range(left, right):
        if nums[i] <= pivot_element:
            nums[i], nums[pointer] = nums[pointer], nums[i]
            pointer += 1

    #   Swap the right element and the pointer element
    nums[right], nums[pointer] = nums[pointer], nums[right]
    if pointer == index:
        return nums[pointer]
    if pointer > index:
        return quickselect(nums, left, pointer - 1, index)
    if pointer < index:
        return quickselect(nums, pointer + 1, right, index)