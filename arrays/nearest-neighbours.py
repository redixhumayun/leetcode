from math import sqrt
import heapq

def euclidean_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def nearest_neighbours(p_x, p_y, k, n_points):
    """
    Args:
     p_x(int32)
     p_y(int32)
     k(int32)
     n_points(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    min_heap = []
    for index, point in enumerate(n_points):
        distance = euclidean_distance([p_x, p_y], point)
        heapq.heappush(min_heap, (distance, index))
    result = []
    while k > 0:
        (distance, index) = heapq.heappop(min_heap)
        result.append(n_points[index])
        k -= 1
    return result


if __name__ == "__main__":
    p_x = 1
    p_y = 1
    k = 1
    n_points = [[0, 0], [1, 0]]
    result = nearest_neighbours(p_x, p_y, k, n_points)
    print(result)

    p_x = 1
    p_y = 1
    k = 2
    n_points = [[1, 0], [2, 1], [0, 1]]
    result = nearest_neighbours(p_x, p_y, k, n_points)
    print(result)