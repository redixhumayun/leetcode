from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(string, counter):
            if counter < 0 or counter > n or len(string) > n * 2:
                return
            if len(string) == n*2 and counter == 0:
                result.append("".join(string[:]))
                return

            string.append("(")
            backtrack(string, counter + 1)
            string.pop()

            string.append(")")
            backtrack(string, counter - 1)
            string.pop()
            # for choice in choices:
            #     if choice == "(" and counter < n:
            #         string.append("(")
            #         backtrack(string, counter + 1)
            #         string.pop()
            #     elif choice == ")" and counter > 0:
            #         string.append(")")
            #         backtrack(string, counter - 1)
            #         string.pop()
            return result

        choices = ["(", ")"]
        backtrack([], 0)
        return result

if __name__ == "__main__":
    n = 3
    print(Solution().generateParenthesis(n))