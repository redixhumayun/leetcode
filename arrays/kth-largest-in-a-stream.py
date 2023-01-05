import heapq

def kth_largest(k, initial_stream, append_stream):
    """
    Args:
     k(int32)
     initial_stream(list_int32)
     append_stream(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    #   Create the min heap
    min_heap = []
    heapq.heapify(min_heap)
    for num in initial_stream:
        heapq.heappush(min_heap, num)

    #   Remove elements from the heap until there are k elements left
    while len(min_heap) > k:
        heapq.heappop(min_heap)

    output = []
    for num in append_stream:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
        output.append(min_heap[0])
    
    return output

if __name__ == '__main__':
    k = 2
    initial_stream = [4, 6]
    append_stream = [5, 2, 20]
    print(kth_largest(k, initial_stream, append_stream))

    k = 2
    initial_stream = [1000000000]
    append_stream = [100000000]
    print(kth_largest(k, initial_stream, append_stream))

    # k = 3
    # initial_stream = [1, 2, 3, 4, 5]
    # append_stream = [6, 7, 8, 9, 10]
    # print(kth_largest(k, initial_stream, append_stream))

    # k = 1
    # initial_stream = [1, 2, 3, 4, 5]
    # append_stream = [6, 7, 8, 9, 10]
    # print(kth_largest(k, initial_stream, append_stream))

    # k = 5
    # initial_stream = [1, 2, 3, 4, 5]
    # append_stream = [6, 7, 8, 9, 10]
    # print(kth_largest(k, initial_stream, append_stream))