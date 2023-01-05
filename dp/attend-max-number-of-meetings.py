from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        def can_attend_meeting(previous, current):
            return previous[1] <= current[0]

        def dp(index, previous_interval_attended, score):
            if index == len(events):
                return 0
            skip = dp(index + 1, previous_interval_attended, score)
            attend = 0
            if can_attend_meeting(previous_interval_attended, events[index]):
                attend = 1 + dp(index + 1, tuple(events[index]), score + 1)
            return max(skip, attend)
        return dp(0, (0, 0), 0)

if __name__ == "__main__":
    print(Solution().maxEvents([[1,2],[2,3],[3,4]]))
    print(Solution().maxEvents([[1, 5], [2, 3], [3, 4]]))