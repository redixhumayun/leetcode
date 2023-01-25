from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort()

        def overlap(interval_1, interval_2):
            [start_1, end_1] = interval_1
            [start_2, end_2] = interval_2

            if start_2 <= end_1 <= end_2:
                return True

            if start_1 <= start_2 <= end_1:
                return True
            
            return False

        output = []
        output_counter = 0
        i = 0
        while i <= len(intervals) - 1:
            first = None
            second = None

            if output_counter == 0:
                output.append(intervals[i])
                output_counter += 1
                i += 1
                continue
            
            first = output[output_counter - 1]
            second = intervals[i]
                
            if overlap(first, second):
                if first[1] > second[1]:
                    output[output_counter - 1] = [first[0], first[1]]
                else:
                    output[output_counter - 1] = [first[0], second[1]]
            else:
                output.append(second)
                output_counter += 1
            
            i += 1

        return output
            

if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(solution.merge([[1, 4], [4, 5]]))
    print(solution.merge([[1, 4], [0, 4]]))
    print(solution.merge([[1,4],[2,3]]))
    print(solution.merge([[1,4],[0,2],[3,5]]))