import heapq

def online_median(stream):
    """
    Args:
     stream(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    max_heap = []
    min_heap = []
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)

    def findMedian():
        if len(max_heap) == len(min_heap):
            return (abs(max_heap[0]) + min_heap[0]) // 2
        if len(max_heap) - len(min_heap) == 1:
            return abs(max_heap[0])
        else:
            raise Exception('The heaps are in an undefined state')


    output = []
    for number in stream:
        if len(max_heap) == 0:
            heapq.heappush(max_heap, -number)
            output.append(findMedian())
            continue
        if number <= abs(max_heap[0]):
            heapq.heappush(max_heap, -number)
            if len(max_heap) - len(min_heap) > 1:
                r = abs(heapq.heappop(max_heap))
                heapq.heappush(min_heap, r)
        else:
            heapq.heappush(min_heap, number)
            if len(min_heap) - len(max_heap) > 0:
                r = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -r)
        output.append(findMedian())
        
    return output

if __name__ == '__main__':
    stream = [3, 8, 5, 2]
    print(online_median(stream))

    #######
    #   max_heap    min_heap    Median
    #   [3]         []          3
    #   [3]         [8]         3+8/2 = 5
    #   [3]         [5, 8]      
    #   [5, 3]      [8]         5
    #   [5, 3, 2]   [8]         
    #   [3, 2]      [5, 8]      3+5/2 = 4
    #######

    # stream = [5, 15, 1, 3]
    # print(online_median(stream))

    # stream = [2, 4, 7, 1, 5, 3]
    # print(online_median(stream))

    # stream = [2, 4, 7, 1, 5, 3, 8]
    # print(online_median(stream))

    # stream = [2, 4, 7, 1, 5, 3, 8, 10]
    # print(online_median(stream))

    # stream = [2, 4, 7, 1, 5, 3, 8, 10, 11]
    # print(online_median(stream))
