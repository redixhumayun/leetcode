from typing import List
import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #   Convert the list to a 1D list
        flattened_intervals = []
        for interval in intervals:
            flattened_intervals.append(interval[0])
            flattened_intervals.append(interval[1])

        #   Find insertion point for start
        [start, end] = newInterval
        start_index = bisect.bisect_left(flattened_intervals, start)
        if start_index < 0 or start_index >= len(flattened_intervals):
            bisect.insort_left(flattened_intervals, start)
        elif flattened_intervals[start_index] != start:
            bisect.insort_left(flattened_intervals, start)

        end_index = bisect.bisect_left(flattened_intervals, end)
        if end_index < 0 or end_index >= len(flattened_intervals):
            bisect.insort_left(flattened_intervals, end)
        elif flattened_intervals[end_index] != end:
            bisect.insort_left(flattened_intervals, end)

        overlapping_index = [0, 0]
        if start_index % 2 != 0:
            overlapping_index[0] = start_index - 1
        else:
            overlapping_index[0] = start_index

        if (len(flattened_intervals) - 1 - end_index) % 2 != 0:
            overlapping_index[1] = end_index + 1
        else:
            overlapping_index[1] = end_index

        output = []
        result = []
        index = 0
        while index < len(flattened_intervals):
            if index != 0 and len(result) == 2:
                output.append(result)
                result = []
            
            if index == overlapping_index[0]:
                result.append(flattened_intervals[overlapping_index[0]])
                result.append(flattened_intervals[overlapping_index[1]])
                output.append(result)
                result = []
                index = overlapping_index[1] + 1
                continue

            result.append(flattened_intervals[index])
            index += 1

        if len(result) > 0:
            output.append(result)
        return output

if __name__ == '__main__':
    solution = Solution()
    print(solution.insert([[1, 3], [6, 9]], [2, 5]))
    print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print(solution.insert([], [5, 7]))
    print(solution.insert([[1, 5]], [2, 3]))
    print(solution.insert([[1, 5]], [2, 7]))
    print(solution.insert([[0,3],[6,8],[9,12]], [0,4]))