from collections import defaultdict

def find_top_k_frequent_elements(arr, k):
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    # Write your code here.

    #   This solution runs in O(n) time and O(n) space
    #   It uses a hash map as a frequency counter and then uses a 2D array to place elements according
    #   to their frequency where the frequency = index.
    #   Then it iterates over the frequency array and creates the output array based on the value of k
    counter = defaultdict(int)
    for num in arr:
        counter[num] += 1

    #   Find maximum frequency
    max_freq = float("-inf")
    for value in counter.values():
        max_freq = max(max_freq, value)

    #   Create array of frequency + 1 size
    frequency_array = [None] * (int(max_freq) + 1)
    for key, value in counter.items():
        if frequency_array[value] is None:
            frequency_array[value] = [key]  # type: ignore
        elif frequency_array[value] is not None:
            frequency_array[value].append(key)  # type: ignore

    pointer = len(frequency_array) - 1
    output_arr = []
    while k > 0:
        if frequency_array[pointer] is not None:
            for value in frequency_array[pointer]:  # type: ignore
                output_arr.append(value)
                k -= 1
                if k == 0:
                    break
        pointer -= 1
    
    return output_arr


if __name__ == '__main__':
    arr = [1, 1, 1, 2, 2, 3]
    k = 2
    print(find_top_k_frequent_elements(arr, k))

    arr = [100000, 0, 99999, 3, 4, 100000, 0]
    k = 3
    print(find_top_k_frequent_elements(arr, k))