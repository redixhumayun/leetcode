import heapq

class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        max_heap = []
        for num in arr:
            diff = abs(num - x)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-diff, num))
                continue
            if len(max_heap) >= k:
                (current_top_diff, current_top_number) = max_heap[0]
                if diff == abs(current_top_diff):
                    #   Both values will give the same difference
                    #   If new value is smaller, pop and push
                    if num <= current_top_number:
                        heapq.heappop(max_heap)
                        heapq.heappush(max_heap, (-diff, num))
                    #   If new value is larger, ignore it
                elif diff < abs(current_top_diff):
                    #   Put new value
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-diff, num))
        result = []
        print(max_heap)
        for (diff, value) in max_heap:
            result.append(abs(value))
        return sorted(result)

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    k = 4
    x = -1
    print(Solution().findClosestElements(arr, k, x))