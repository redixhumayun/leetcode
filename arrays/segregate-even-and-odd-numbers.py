
def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    first = 0
    last = len(numbers) - 1
    while first < last:
        if numbers[first] == 1 or numbers[first] % 2 == 1:
            #   If the left number is odd
            if numbers[last] % 2 == 0:
                #   If the right number is even
                numbers[first], numbers[last] = numbers[last], numbers[first]
                first += 1
                last -= 1
            else:
                last -= 1
        else:
            first += 1
    return numbers


if __name__ == '__main__':
    print(segregate_evens_and_odds([1, 2, 3, 4]))
    print(segregate_evens_and_odds([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(segregate_evens_and_odds([1, 3, 5, 7, 9]))
    print(segregate_evens_and_odds([2, 4, 6, 8, 10]))