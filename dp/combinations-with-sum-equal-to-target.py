
def generate_all_combinations(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    # def recurse(curr, index):
    #     if sum(curr) > target:
    #         return
    #     if sum(curr) == target:
    #         ans.add(tuple(curr[:]))
    #         return
    #     if index >= len(arr):
    #         return
    #     curr.append(arr[index])
    #     recurse(curr, index + 1)
    #     curr.pop()
    #     recurse(curr, index + 1)

    def recurse(curr, index):
        if sum(curr) > target:
            return
        if sum(curr) == target:
            ans.add(tuple(curr[:]))
            return
        for i in range(index, len(arr)):
            if sum(curr) + arr[i] <= target:
                curr.append(arr[i])
                recurse(curr, i + 1)
                curr.pop()
    ans = set()
    recurse([], 0)
    output = [list(a) for a in ans]
    return output


if __name__ == "__main__":
    arr = [1, 2, 3]
    target = 3
    result = generate_all_combinations(arr, target)
    print(result)

    arr = [1, 1, 1, 1]
    target = 2
    result = generate_all_combinations(arr, target)
    print(result)

    # arr = [94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94]
    # target = 2256
    # result = generate_all_combinations(arr, target)
    # print(result)