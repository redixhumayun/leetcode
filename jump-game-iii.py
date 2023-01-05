from collections import deque

class Solution:
    def canReach(self, arr, start: int) -> bool:
        def valid(index):
            return 0 <= index < len(arr)

        def possible_indexes(index):
            return [index + arr[index], index - arr[index]]

        queue = deque([start])
        seen = {start}
        while queue:
            current_index = queue.popleft()
            if arr[current_index] == 0:
                return True
            for index in possible_indexes(current_index):
                if valid(index):
                    if index not in seen:
                        seen.add(index)
                        queue.append(index)
        return False


if __name__ == '__main__':
    arr = [4,2,3,0,3,1,2]
    start = 0
    print(Solution().canReach(arr, start))