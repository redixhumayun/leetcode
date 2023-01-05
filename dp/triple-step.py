from collections import defaultdict

def triple_step(n):
    hash_map = defaultdict(int)
    #   This is the top-down DP solution
    def recurse_with_memoization(steps):
        if steps < 0:
            return 0
        if steps == 0:
            return 1
        if steps in hash_map:
            return hash_map[steps]
        score = 0
        for num in (1, 2, 3):
            score += recurse_with_memoization(steps - num)
        hash_map[steps] = score
        return hash_map[steps]

    #   This is the backtracking solution with memoization which builds up from the bottom
    def recurse(curr, steps):
        if steps > n:
            return 0
        if steps == n:
            ans.append(curr[:])
            return 1
        if steps in hash_map:
            return hash_map[steps]
        score = 0
        for num in (1, 2, 3):
            curr.append(num)
            score += recurse(curr, steps + num)
            curr.pop()
        hash_map[steps] = score
        return score
    ans = []
    result = recurse([], 0)
    # result = recurse_with_memoization(n)
    return result

if __name__ == "__main__":
    print(triple_step(25))