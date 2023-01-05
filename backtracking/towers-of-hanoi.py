count = 0
ans = []


def tower_of_hanoi(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    ans = []
    def helper(n, source, dest, aux):
        if n == 1:
            ans.append([source, dest])
            return
        helper(n - 1, source, aux, dest)
        ans.append([source, dest])
        helper(n - 1, aux, dest, source)
    helper(n, 1, 3, 2)
    return ans

# def towers_of_hanoi(n, source, dest, aux):
#     global count
#     global ans
#     if n == 1:
#         count += 1
#         ans.append([source, dest])
#         print(f"Moving {n} from {source} to {dest}")
#         return
#     towers_of_hanoi(n - 1, source, aux, dest)
#     count += 1
#     ans.append([source, dest])
#     print(f"Moving {n} from {source} to {dest}")
#     towers_of_hanoi(n - 1, aux, dest, source)

if __name__ == "__main__":
    result = tower_of_hanoi(4)
    print(result)