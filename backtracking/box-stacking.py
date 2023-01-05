from collections import defaultdict
from functools import cache

def box_stacking(boxes):
    boxes.sort(reverse=True)

    def can_box_be_stacked(previous, box):
        if previous is None:
            #   If this is the first box that will be stacked
            return True
        previous_box = previous
        (width, height, breadth) = previous_box
        (w, h, b) = box
        if width > w and height > h and breadth > b:
            return True
        return False

    #   This is the solution where the option of taking a box or skipping
    #   a box is considered. Results in an O(2^n) solution
    @cache
    def stack_boxes(index, height, bottom):
        if index >= len(boxes):
            return height
        take_box = 0
        if can_box_be_stacked(bottom, boxes[index]):
            take_box = stack_boxes(index + 1, height + boxes[index][1], boxes[index])
        skip_box = stack_boxes(index + 1, height, bottom)
        result = max(take_box, skip_box)
        return result

    total_height = stack_boxes(0, 0, None)
    return total_height
    
    # def backtrack(curr, index, stack_height):
    #     nonlocal ans_height
    #     if index >= len(boxes):
    #         ans_height = max(ans_height, stack_height)
    #         ans.append(curr[:])
    #         return 0
    #     if (boxes[index][0], boxes[index][1], boxes[index][2]) in hash_map:
    #         return hash_map[(boxes[index][0], boxes[index][1], boxes[index][2])]
    #     f_height = 0
    #     for i in range(index, len(boxes)):
    #         height = 0
    #         if can_box_be_stacked(curr, boxes[i]):
    #             curr.append(boxes[i])
    #             height += boxes[i][1] + backtrack(curr, i + 1, stack_height + boxes[i][1])
    #             f_height = max(height, f_height)
    #             curr.pop()
    #     hash_map[(boxes[index][0], boxes[index][1], boxes[index][2])] = f_height
    #     return hash_map[(boxes[index][0], boxes[index][1], boxes[index][2])]
    # ans = []
    # ans_height = 0
    # hash_map = defaultdict(int)
    # total_height = backtrack([], 0, 0)
    # return total_height

if __name__ == '__main__':
    boxes = [(5, 6, 7), (1, 2, 3), (4, 8, 6), (10, 12, 32)]
    print(box_stacking(boxes))