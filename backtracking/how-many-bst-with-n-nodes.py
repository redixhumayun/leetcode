class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def print_tree(self, root):
        if root is not None:
            print(root.val)
            self.print_tree(root.left)
            self.print_tree(root.right)

def how_many_bsts(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    #   This approach uses an algorithm that divides the array into the left and right subtrees
    #   based on which index has the root node. Not sure of the complexity
    def recurse(root, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return 2
        
        score = 0
        for i in range(len(nums)):
            root = nums[i]
            left = nums[:i]
            right = nums[i+1:]
            left_subtree = recurse(root, left)
            right_subtree = recurse(root, right)
            ans = None
            if left_subtree == 0 or right_subtree == 0:
                ans = max(left_subtree, right_subtree)
            else:
                ans = left_subtree * right_subtree
            score += ans
        return score
        
    ans = recurse(None, [i+1 for i in range(n)])
    return ans

    #   This is the exhaustive approach, where all possible permutations are found
    #   and then each permutation is checked to see if it is a valid binary tree and if it is,
    #   added to a set as a pre-order traversal. Each new binary tree is compared to the set.
    #   Problem is complexity = O(n!) -> complexity of constructing all permutations
    # def construct_bst(arr):
    #     def insert(root: BST | None, value) -> BST:
    #         if not root:
    #             root = BST(value)
    #             return root
    #         if value <= root.val:
    #             root.left = insert(root.left, value)
    #         else:
    #             root.right = insert(root.right, value)
    #         return root
            
    #     root = BST(arr[0])
    #     for i in range(1, len(arr)):
    #         insert(root, arr[i])
    #     return root

    # def is_bst_new(root, seen):
    #     ans = []
    #     def pre_order_traversal(root):
    #         if root:
    #             ans.append(root.val)
    #             pre_order_traversal(root.left)
    #             pre_order_traversal(root.right)
    #     pre_order_traversal(root)
    #     if tuple(ans) not in seen:
    #         seen.add(tuple(ans))

    # def backtrack(curr, nums):
    #     if len(curr) == n:
    #         ans.append(curr[:])
    #         return
    #     for i in range(len(nums)):
    #         curr.append(nums[i])
    #         backtrack(curr, nums[:i] + nums[i+1:])
    #         curr.pop()
    
    # arr = [i+1 for i in range(n)]
    # ans = []
    # backtrack([], arr)
    # seen = set()
    # for a in ans:
    #     root = construct_bst(a)
    #     is_bst_new(root, seen)
    # print(seen)
    # return len(seen)


if __name__ == '__main__':
    print(how_many_bsts(1))
    print(how_many_bsts(2))
    print(how_many_bsts(3))
    print(how_many_bsts(4))
    print(how_many_bsts(5))
    print(how_many_bsts(16))