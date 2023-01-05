def string_permutations(string):
    ans = []
    def backtrack(curr, s):
        if len(s) == 0:
            ans.append(curr[:])
            return
        # if len(curr) == len(string):
        #     ans.append(curr[:])
        #     return
        for index, char in enumerate(s):
            # curr.append(char)
            backtrack(curr + char, s[:index] + s[index + 1:])
            # curr.pop()
    backtrack("", string)
    # ans = list(map(lambda x: "".join(map(str, x)), ans))
    print(ans)

if __name__ == "__main__":
    string = "abc"
    print(string_permutations(string))