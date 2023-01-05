from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        mapping = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        def backtrack(curr, index):
            if len(curr) == len(digits):
                ans.append(curr[:])
                return
            for char in mapping[digits[index]]:
                curr.append(char)
                backtrack(curr, index + 1)
                curr.pop()
        ans = []
        digits = "".join([c for c in digits if c != "1"])
        backtrack([], 0)
        results = []
        for a in ans:
            results.append("".join(a))
        return results

if __name__ == "__main__":
    s = Solution()
    # print(s.letterCombinations("21"))
    print(s.letterCombinations("1234567"))
    # print(s.letterCombinations("2"))
    # print(s.letterCombinations(""))