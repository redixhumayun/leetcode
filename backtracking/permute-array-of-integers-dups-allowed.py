from collections import Counter

def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    ans = []
    def backtrack(curr, counter):
        if len(curr) == len(arr):
            ans.append(curr[:])
            return
        for num in counter:
            if counter[num] > 0:
                curr.append(num)
                counter[num] -= 1
                backtrack(curr, counter)
                counter[num] += 1
                curr.pop()
        # for index, num in enumerate(array):
        #     curr.append(num)
        #     backtrack(curr, array[:index] + array[index+1:], counter)
        #     curr.pop()
    cnt = Counter(arr)
    backtrack([], cnt)
    return ans

if __name__ == "__main__":
    arr = [1, 1, 2]
    result = get_permutations(arr)
    print(result)

    # arr = [1, 2, 3]
    # result = get_permutations(arr)
    # print(result)

    # arr = [1, 2, 2]
    # result = get_permutations(arr)
    # print(result)