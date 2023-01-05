from functools import cmp_to_key

def compare(array_1, array_2):
    return array_1[0] - array_2[0]

def can_attend_all_meetings(intervals):
    """
    Args:
     intervals(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    sorted(intervals, key=cmp_to_key(compare))
    for index in range(len(intervals) - 1):
        current_meeting = intervals[index]
        next_meeting = intervals[index + 1]
        if current_meeting[1] > next_meeting[0]:
            return 0
    return 1


if __name__ == '__main__':
    print(can_attend_all_meetings([[1, 5], [5, 8], [10, 15]]))
    print(can_attend_all_meetings([[0, 30], [5, 10], [15, 20]]))