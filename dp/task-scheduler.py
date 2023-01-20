from typing import List
from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Greedy approach
        """
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1
        
        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n
        
        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)



        # if n == 0:
        #     return len(tasks)

        # #   Build counter for tasks
        # tasks_counter = defaultdict(tuple)
        # for task in tasks:
        #     if task in tasks_counter:
        #         (count, cooldown) = tasks_counter[task]
        #         tasks_counter[task] = (count + 1, cooldown)
        #     else:
        #         tasks_counter[task] = (1, 0)


        # def find_max_in_tasks_counter():
        #     max_value = float("-inf")
        #     max_key = None
        #     for key, value in tasks_counter.items():
        #         (count, cooldown) = value
        #         if cooldown > 0:
        #             continue
        #         if count > max_value:
        #             max_value = count
        #             max_key = key

        #     return max_key

        # def reduce_cooldown_on_all_tasks(exception_key):
        #     for key, value in tasks_counter.items():
        #         (count, cooldown) = value
        #         if key == exception_key:
        #             continue
        #         if cooldown > 0:
        #             tasks_counter[key] = (count, cooldown - 1)

        # count = 0
        # while len(tasks_counter) > 0:
        #     key_to_pick = find_max_in_tasks_counter()
        #     if key_to_pick is None:
        #         count += 1
        #         reduce_cooldown_on_all_tasks(None)
        #         continue

        #     (key_count, cooldown) = tasks_counter[key_to_pick]
        #     if key_count == 1:
        #         del tasks_counter[key_to_pick]
        #     else:
        #         tasks_counter[key_to_pick] = (key_count - 1, n)
        #     reduce_cooldown_on_all_tasks(key_to_pick)
        #     count += 1
        # return count



if __name__ == "__main__":
    print(Solution().leastInterval(["A","A","A","B","B","B"], 2))
    print(Solution().leastInterval(["A","A","A","B","B","B"], 0))
    print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))