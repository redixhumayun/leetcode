from collections import deque

class Solution:
    def openLock(self, deadends, target: str) -> int:
        queue = deque()
        queue.append(('0000', 0))  #   string, steps
        seen = set()
        seen.add('0000')
        ans = float("inf")

        if '0000' in deadends:
            return -1

        while queue:
            current_string, steps = queue.popleft()
            if current_string == target:
                ans = min(ans, steps)
            for index in range(len(current_string)):
                incremented_string = current_string[:index] + str((int(current_string[index]) + 1)%10) + current_string[index+1:]
                decremented_string = current_string[:index] + str((int(current_string[index]) - 1)%10) + current_string[index+1:]
                if incremented_string not in seen:
                    seen.add(incremented_string)
                    if incremented_string not in deadends:
                        queue.append((incremented_string, steps + 1))
                if decremented_string not in seen:
                    seen.add(decremented_string)
                    if decremented_string not in deadends:
                        queue.append((decremented_string, steps + 1))
        
        if ans == float("inf"):
            return -1
        return ans

if __name__ == '__main__':
    deadends = ["0000"]
    target = "8888"
    print(Solution().openLock(deadends, target))