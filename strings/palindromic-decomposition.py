
def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    def is_palindrome(curr):
        first_index = curr[0]
        last_index = curr[-1]
        while first_index <= last_index:
            if s[first_index] == s[last_index]:
                first_index += 1
                last_index -= 1
            else:
                return False
        return True

    def backtrack(curr, i):
        if i >= len(s):
            return
        for j in range(i, len(s)):
            curr.append(j)
            if is_palindrome(curr):
                index_pairs.add((curr[0], curr[-1]))
            backtrack(curr, j+1)
            curr.pop()
    ans = []
    index_pairs = set()
    backtrack([], 0)
    for pair in index_pairs:
        string = ""
        first, last = pair
        if first != last:
            if first != 0:
                string += "|".join(list(s[:first])) + "|"

            string += s[first:last+1]

            if last != len(s) - 1:
                string += '|' + "|".join(list(s[last+1:]))
            ans.append(string)
    ans.append("|".join(list(s)))
    return ans


if __name__ == '__main__':
    print(generate_palindromic_decompositions("abracadabra"))
    print(generate_palindromic_decompositions("aab"))
    print(generate_palindromic_decompositions("a"))
    print(generate_palindromic_decompositions("abcdcba"))
    print(generate_palindromic_decompositions("xyy"))